import cv2
import numpy as np
from .key import press
from collections import namedtuple


Pixel = namedtuple('Pixel', ['xy', 'rgb'])


class Skill(object):
    def __init__(self, *pixels, image=None, mask=None, hotkey=None, successor=None):
        super(Skill, self).__init__()
        self.__load_match(pixels, image, mask)
        self.hotkey = hotkey
        self.successor = successor

    def __load_match(self, pixels, image, mask):
        if pixels:
            self.match = lambda region: region.match(pixels)
            return
        if image is None:
            self.match = lambda region: True
            return
        if mask is None:
            template = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
            self.match = lambda region: region.match(template)
            return
        template = cv2.imread(image, cv2.IMREAD_COLOR)
        mask = (template[:, :, 0] != mask[0]) | (template[:, :, 1] != mask[1]) | (template[:, :, 2] != mask[2])
        mask = mask.astype(np.uint8)
        mask = np.expand_dims(mask, axis=-1).repeat(3, axis=-1)
        self.match = lambda region: region.match(template, mask)

    def cast(self, region):
        if self.match(region):
            if self.hotkey:
                press(self.hotkey)
            return
        if self.successor:
            self.successor.cast(region)
