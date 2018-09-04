from elf.region import RegionRelativePixel
from .九灵 import *


class _状态(object):

    def __init__(self):
        super(_状态, self).__init__()
        self.macro = 如梦令
        如梦令.successor = 同心一命
        同心一命.successor = 聚蛊

    def execution(self):
        region = RegionRelativePixel(865, 985, 148, 47)
        self.macro.cast(region)


状态 = _状态()
