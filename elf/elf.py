import cv2
import numpy as np
from PIL import ImageGrab


def find_pics(images, region=None, precision=0.9, mask=None):
    """Finds for images within an area
    除非是要找透明图, 否则不应该使用 mask, 制作 mask 时需要消耗时间

    type:
    images: List [string], path to the image file
    region: tupe(x, y, width, height), default is the entire screen
    precision: float, 0 ~ 1, matching precision, default is 0.9
    mask: tupe(B, G, R), these pixels will be ignored when scanning, default is don't ignored

    rtype: Iterator [tupe(x, y)], corresponds to input one by one
    """
    edged = cv2.cvtColor(np.array(ImageGrab.grab(region)), cv2.COLOR_RGB2GRAY)
    if mask is None:
        return map(lambda image: __match(edged, image, precision), images)
    return map(lambda image: __match_by_mask(edged, image, precision, mask), images)


def find_pic(image, region=None, precision=0.9, mask=None):
    """Finds for an image within an area
    除非是要找透明图, 否则不应该使用 mask, 制作 mask 时需要消耗时间

    type:
    image: string, path to the image file
    region: tupe(x, y, width, height), default is the entire screen
    precision: float, 0 ~ 1, matching precision, default is 0.9
    mask: tupe(B, G, R), these pixels will be ignored when scanning, default is don't ignored

    rtype: tupe(x, y), if don't found return None
    """
    edged = cv2.cvtColor(np.array(ImageGrab.grab(region)), cv2.COLOR_RGB2BGR)
    if mask is None:
        return __match(edged, image, precision)
    return __match_by_mask(edged, image, precision, mask)


def __match(edged, image, precision):
    template = cv2.imread(image, cv2.IMREAD_COLOR)
    locations = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF_NORMED)
    return __best_point(locations, precision)


def __match_by_mask(edged, image, precision, mask):
    template = cv2.imread(image, cv2.IMREAD_COLOR)
    mask = (template[:, :, ] != mask)
    mask = mask.astype(np.uint8)
    locations = cv2.matchTemplate(edged, template, cv2.TM_CCORR_NORMED, mask=mask)
    return __best_point(locations, precision)


def __best_point(locations, precision):
    _, max_val, _, max_loc = cv2.minMaxLoc(locations)
    if max_val < precision:
        return None
    return max_loc
