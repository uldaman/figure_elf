from .冲劲寸拳 import 冲劲寸拳
from elf.region import RegionRelativePixel
from elf.skill import (
    Skill,
    Pixel,
)


class _群攻(object):

    def __init__(self):
        super(_群攻, self).__init__()
        # 狮吼 = Skill(
        #     Pixel((), ()),
        #     Pixel((), ()),
        #     Pixel((), ()),
        #     Pixel((), ()),
        #     Pixel((), ()),
        #     Pixel((), ()),
        #     Pixel((), ()),
        #     hotkey='5',
        # )
        升龙拳 = Skill(
            Pixel((17, 11), (0xA7, 0x94, 0x31)),
            Pixel((-2, 13), (0x9D, 0x33, 0x2D)),
            Pixel((9, 4), (0xE0, 0xDA, 0x6F)),
            Pixel((13, 19), (0xB1, 0x56, 0x30)),
            Pixel((11, 25), (0xF7, 0xFA, 0xF4)),
            Pixel((4, 24), (0x90, 0x47, 0x25)),
            Pixel((-6, 18), (0xFF, 0xF3, 0xEA)),
            hotkey='6',
        )
        无影拳 = Skill(
            Pixel((67, 9), (0x68, 0x38, 0x24)),
            Pixel((7, 0), (0xDE, 0xB5, 0x60)),
            Pixel((14, 7), (0xDF, 0xC5, 0x5F)),
            Pixel((14, 16), (0xAB, 0x7B, 0x40)),
            Pixel((11, 22), (0x50, 0x2D, 0x18)),
            Pixel((1, 22), (0x9E, 0x69, 0x39)),
            Pixel((-5, 12), (0xD6, 0x8C, 0x40)),
            hotkey='7',
        )
        裂地斩 = Skill(
            Pixel((116, 12), (0x86, 0x7C, 0x50)),
            Pixel((10, 0), (0xE3, 0xC6, 0x70)),
            Pixel((13, 4), (0xD0, 0xA0, 0x64)),
            Pixel((14, 9), (0xDC, 0xB2, 0x6B)),
            Pixel((16, 16), (0xBF, 0xAD, 0x61)),
            Pixel((4, 18), (0x54, 0x3E, 0x23)),
            Pixel((-4, 11), (0xEC, 0xE6, 0x87)),
            hotkey='8',
        )
        旋风腿 = Skill(
            Pixel((166, 11), (0xBD, 0x82, 0x52)),
            Pixel((4, 0), (0xC9, 0x96, 0x61)),
            Pixel((10, 5), (0x76, 0x43, 0x29)),
            Pixel((14, 11), (0x5E, 0x41, 0x2F)),
            Pixel((14, 20), (0xE5, 0xC8, 0x71)),
            Pixel((7, 22), (0xE9, 0xE0, 0x82)),
            Pixel((-5, 20), (0xEF, 0xE9, 0xB4)),
            hotkey='9',
        )
        # 劈云拳 = Skill(
        #     hotkey='0',
        # )
        # 狮吼.successor = 升龙拳
        升龙拳.successor = 无影拳
        无影拳.successor = 裂地斩
        裂地斩.successor = 旋风腿
        # 旋风腿.successor = 劈云拳
        self.macro = 升龙拳

    def execution(self):
        冲劲寸拳.execution()
        region = RegionRelativePixel(965, 985, 243, 47)
        self.macro.cast(region)


群攻 = _群攻()
