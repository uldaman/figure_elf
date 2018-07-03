from elf.skill import Skill
from elf.region import RegionImage


class _冲劲寸拳(object):

    def __init__(self):
        super(_冲劲寸拳, self).__init__()
        self.macro = Skill(image=r"C:\Users\HanXiao\Desktop\cjcq.bmp", hotkey='f1')

    def execution(self):
        region = RegionImage(708, 938, 50, 50)
        self.macro.cast(region)


冲劲寸拳 = _冲劲寸拳()
