from .key import press
from collections import namedtuple


Pixel = namedtuple('Pixel', ['xy', 'rgb'])


class Skill(object):
    def __init__(self, *pixels, hotkey=None, successor=None):
        super(Skill, self).__init__()
        self.pixels = pixels
        self.hotkey = hotkey
        self.successor = successor

    def cast(self, region):
        if all(map(lambda pixel: region.match(pixel), self.pixels)):
            if self.hotkey:
                press(self.hotkey)
        else:
            if self.successor:
                self.successor.cast(region)
