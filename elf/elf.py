import cv2
import numpy as np
from PIL import ImageGrab


def find_pic(image, region=None, mask=None, precision=0.9):
    """Searchs for an image within an area

    type :
    image : string, path to the image file
    region: tupe(x, y, width, height), default is the entire screen
    mask: tupe(B, G, R), these pixels will be ignored when scanning, default is don't ignored
    precision : float, 0 ~ 1, matching precision, default is 0.9

    rtype : tupe(x, y), if don't found return None
    """
    edged = cv2.cvtColor(np.array(ImageGrab.grab(region)), cv2.COLOR_RGB2GRAY)

    if mask is None:
        template = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    else:
        template = cv2.imread(image, cv2.IMREAD_COLOR)
        mask = (template[:, :, 0] != mask[0]) & (template[:, :, 1] != mask[1]) & (template[:, :, 2] != mask[2])
        mask = mask.astype(np.uint8)
        template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(edged, template, cv2.TM_CCORR_NORMED, mask=mask)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if max_val < precision:
        return None
    return max_loc


if __name__ == '__main__':
    for i in range(0, 10):
        point = find_pic("elf/123.bmp", (0, 0, 500, 500), (255, 255, 255))
        print(point)

    for i in range(0, 10):
        print(i)
