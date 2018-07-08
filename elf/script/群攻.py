from .冲劲寸拳 import 冲劲寸拳
from elf.region import RegionRelativePixel
from .技能 import *


class _群攻(object):

    def __init__(self):
        super(_群攻, self).__init__()
        self.macro = 狮吼
        狮吼.successor = 升龙拳
        升龙拳.successor = 无影拳
        无影拳.successor = 裂地斩
        裂地斩.successor = 旋风腿
        旋风腿.successor = 开山拳
        开山拳.successor = 炼火拳
        炼火拳.successor = 横扫
        横扫.successor = 劈云拳

    def execution(self):
        冲劲寸拳.execution()
        region = RegionRelativePixel(815, 985, 392, 47)
        self.macro.cast(region)


群攻 = _群攻()
