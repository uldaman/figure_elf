from elf.region import RegionRelativePixel
from .九灵 import *


class _攻击(object):

    def __init__(self):
        super(_攻击, self).__init__()
        self.macro = 灵犀三现1
        灵犀三现1.successor = 灵犀三现2
        灵犀三现2.successor = 灵犀三现3
        灵犀三现3.successor = 破梦
        破梦.successor = 普攻

    def execution(self):
        region = RegionRelativePixel(1011, 985, 96, 47)
        self.macro.cast(region)


攻击 = _攻击()
