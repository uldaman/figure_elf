import cv2
import numpy as np
from .key import press
from collections import namedtuple


Pixel = namedtuple('Pixel', ['xy', 'rgb'])


class Skill(object):
    def __init__(self, multi_pixel=None, image=None, mask=None, hotkey=None, successor=None):
        super(Skill, self).__init__()
        self.__load_match(multi_pixel, image, mask)
        self.hotkey = hotkey
        self.successor = successor

    def __load_match(self, multi_pixel, image, mask):
        if multi_pixel:
            pixels = SkillFactory(multi_pixel)
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


def SkillFactory(multi_pixel):
    def _analyze_rgb(rgb):
        return (int(rgb[:2], 16), int(rgb[2:4], 16), int(rgb[4:6], 16))

    pixels_str = multi_pixel.split(",")
    pixels = [None] * len(pixels_str)
    pixels[0] = Pixel((), _analyze_rgb(pixels_str[0]))
    for index, pixel_str in enumerate(pixels_str[1:]):
        pixel_list = pixel_str.split("|")
        x = int(pixel_list[0])
        y = int(pixel_list[1])
        pixels[index + 1] = Pixel((x, y), _analyze_rgb(pixel_list[2]))

    return pixels
