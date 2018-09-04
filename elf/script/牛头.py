from elf.skill import Skill
from elf.region import RegionRelativePixel


大地粉碎 = Skill("064574,5|0|064574", hotkey='q')


class _二连(object):

    def __init__(self):
        super(_二连, self).__init__()
        self.macro = 大地粉碎

    def execution(self):
        region = RegionRelativePixel(793, 943, 66, 66)
        self.macro.cast(region)


二连 = _二连()
