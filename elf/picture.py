import cv2
import numpy as np
from PIL import ImageGrab


def find_pics(images, region=None, precision=0.9, mask=None):
    """Finds for images within an area
    除非是要找透明图, 否则不应该使用 mask

    type:
    images: List [string], path to the image file
    region: tupe(x, y, width, height), default is the entire screen
    precision: float, 0 ~ 1, matching precision, default is 0.9
    mask: tupe(B, G, R), these pixels will be ignored when scanning, default is don't ignored

    rtype: Iterator [tupe(x, y)], corresponds to input one by one
    """
    if mask is None:
        edged = cv2.cvtColor(np.array(ImageGrab.grab(region)), cv2.COLOR_RGB2GRAY)
        return map(lambda image: __match(edged, image, precision), images)

    edged = cv2.cvtColor(np.array(ImageGrab.grab(region)), cv2.COLOR_RGB2BGR)
    return map(lambda image: __match_by_mask(edged, image, precision, mask), images)


def find_pic(image, region=None, precision=0.9, mask=None):
    """Finds for an image within an area
    除非是要找透明图, 否则不应该使用 mask

    type:
    image: string, path to the image file
    region: tupe(x, y, width, height), default is the entire screen
    precision: float, 0 ~ 1, matching precision, default is 0.9
    mask: tupe(B, G, R), these pixels will be ignored when scanning, default is don't ignored

    rtype: tupe(x, y), if don't found return None
    """
    if mask is None:
        edged = cv2.cvtColor(np.array(ImageGrab.grab(region)), cv2.COLOR_RGB2GRAY)
        return __match(edged, image, precision)

    edged = cv2.cvtColor(np.array(ImageGrab.grab(region)), cv2.COLOR_RGB2BGR)
    return __match_by_mask(edged, image, precision, mask)


def __match(edged, image, precision):
    """匹配图像

    无遮挡匹配， 应用灰度图匹配
    """
    template = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    locations = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF_NORMED)
    return __best_point(locations, precision)


def __match_by_mask(edged, image, precision, mask):
    """匹配图像

    有遮挡匹配， 应用 BGR 匹配， 灰度图误差太大
    """
    template = cv2.imread(image, cv2.IMREAD_COLOR)
    # mask = (template[:, :, ] != mask)  下面这种方式匹配度更高
    mask = (template[:, :, 0] != mask[0]) | (template[:, :, 1] != mask[1]) | (template[:, :, 2] != mask[2])
    mask = mask.astype(np.uint8)
    mask = np.expand_dims(mask, axis=-1).repeat(3, axis=-1)
    locations = cv2.matchTemplate(edged, template, cv2.TM_CCORR_NORMED, mask=mask)
    return __best_point(locations, precision)


def __best_point(locations, precision):
    _, max_val, _, max_loc = cv2.minMaxLoc(locations)
    if max_val < precision:
        return None
    return max_loc


#######################


if __name__ == '__main__':
    # pos = find_pic(r"C:\Users\HanXiao\Desktop\1.bmp", region=(708, 938, 708 + 50, 938 + 50))
    # print(pos)
    import pyautogui
    import time
    time.sleep(2)
    pyautogui.press("a")
    # pyautogui.moveTo(*pos)
    # cv2.waitKey(0)

    # class Region(object):

    #     def __init__(self):
    #         super(Re, self).__init__()
    #         self.arg = arg

    #     def decorate(self, component):

    # class Skill(object):

    #     def __init__(self, image, button):
    #         super(Skill, self).__init__()
    #         self.template = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    #         self.cooling = False

    # cd_seq = []
    # cast_seq = reversed(cd_seq)