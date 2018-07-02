from .elf import __best_point
import cv2
import time
from .key import press
import numpy as np
from PIL import ImageGrab

template1 = cv2.imread(r"C:\Users\HanXiao\Desktop\2.bmp", cv2.IMREAD_GRAYSCALE)
template2 = cv2.imread(r"C:\Users\HanXiao\Desktop\3.bmp", cv2.IMREAD_GRAYSCALE)
region1 = (1118, 990, 1111 + 40, 984 + 40)
region2 = (1166, 990, 1166 + 30, 990 + 30)

while True:
    edged1 = cv2.cvtColor(np.array(ImageGrab.grab(region1)), cv2.COLOR_RGB2GRAY)
    locations1 = cv2.matchTemplate(edged1, template1, cv2.TM_CCOEFF_NORMED)
    pos1 = __best_point(locations1, 0.9)
    if pos1 is None:
        edged2 = cv2.cvtColor(np.array(ImageGrab.grab(region2)), cv2.COLOR_RGB2GRAY)
        locations2 = cv2.matchTemplate(edged2, template2, cv2.TM_CCOEFF_NORMED)
        pos2 = __best_point(locations2, 0.9)
        if pos2:
            press('v')
    time.sleep(0.2)
