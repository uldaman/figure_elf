from .elf import __best_point
import cv2
import time
from .key import press
import numpy as np
from PIL import ImageGrab

template = cv2.imread(r"C:\Users\HanXiao\Desktop\1.bmp", cv2.IMREAD_GRAYSCALE)
region = (708, 938, 708 + 50, 938 + 50)

while True:
    edged = cv2.cvtColor(np.array(ImageGrab.grab(region)), cv2.COLOR_RGB2GRAY)
    locations = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF_NORMED)
    pos = __best_point(locations, 0.9)
    if pos:
        press('f1')
    time.sleep(0.2)
