from elf.region import RegionPixel
from elf.skill import (
    Skill,
    Pixel,
)


class _测试(object):

    def __init__(self):
        super(_测试, self).__init__()
        游龙盘打 = Skill(
            Pixel((13, 13), (0x9F, 0x81, 0x16)),
            Pixel((18, 13), (0xA7, 0x80, 0x2D)),
            Pixel((26, 13), (0xD5, 0xC7, 0x65)),
            Pixel((30, 19), (0xB0, 0x88, 0x36)),
            Pixel((32, 26), (0xF3, 0xF2, 0xAA)),
            Pixel((24, 31), (0xC4, 0xB8, 0x77)),
            Pixel((15, 31), (0xF0, 0xF5, 0xBF)),
            Pixel((11, 23), (0x82, 0x66, 0x23)),
            hotkey='q',
        )
        升龙拳 = Skill(
            Pixel((109, 9), (0x1E, 0x09, 0x05)),
            Pixel((116, 9), (0xC4, 0x99, 0x2B)),
            Pixel((123, 9), (0xBF, 0x7E, 0x24)),
            Pixel((130, 12), (0x1B, 0x08, 0x08)),
            Pixel((130, 22), (0x2E, 0x0D, 0x0B)),
            Pixel((122, 31), (0xD1, 0x9E, 0x45)),
            Pixel((111, 28), (0xDF, 0xE4, 0x7C)),
            Pixel((106, 16), (0x3A, 0x14, 0x0C)),
            hotkey='r',
        )
        炼火拳 = Skill(
            Pixel((158, 9), (0x31, 0x1C, 0x18)),
            Pixel((166, 9), (0x95, 0x6A, 0x41)),
            Pixel((173, 9), (0xC9, 0x95, 0x57)),
            Pixel((179, 14), (0x69, 0x4F, 0x37)),
            Pixel((182, 31), (0xAF, 0x81, 0x50)),
            Pixel((169, 31), (0xD6, 0xA6, 0x63)),
            Pixel((154, 28), (0xF8, 0xF3, 0xC8)),
            Pixel((159, 17), (0xE1, 0xD3, 0x73)),
            hotkey='c',
        )
        游龙盘打.successor = 升龙拳
        升龙拳.successor = 炼火拳
        self.macro = 升龙拳

    def execution(self):
        region = RegionPixel(965, 985, 243, 47)
        self.macro.cast(region)


测试 = _测试()
