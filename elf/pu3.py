# from .elf import __best_point
# import cv2
# import time
# from .key import press
# import numpy as np
# from PIL import ImageGrab

# ImageGrab.grab((965, 985, 965 + 243, 985 + 47)).save(r"C:\Users\HanXiao\Desktop\4.bmp")

from .font import pixel, pixels
from PIL import ImageGrab
from .key import press
import time


class Region(object):

    def __init__(self, region):
        super(Region, self).__init__()
        self.region = region
        self.ylpd = pixels(  # 游龙盘打
            'q',
            pixel((13, 13), (0x9F, 0x81, 0x16)),
            pixel((18, 13), (0xA7, 0x80, 0x2D)),
            pixel((26, 13), (0xD5, 0xC7, 0x65)),
            pixel((30, 19), (0xB0, 0x88, 0x36)),
            pixel((32, 26), (0xF3, 0xF2, 0xAA)),
            pixel((24, 31), (0xC4, 0xB8, 0x77)),
            pixel((15, 31), (0xF0, 0xF5, 0xBF)),
            pixel((11, 23), (0x82, 0x66, 0x23)),
        )
        self.ql = pixels(  # 擒龙
            'e',
            pixel((76, 7), (0xA7, 0x8A, 0x51)),
            pixel((86, 13), (0xB6, 0x90, 0x4E)),
            pixel((87, 25), (0x9C, 0x73, 0x42)),
            pixel((84, 38), (0x4D, 0x4B, 0x5A)),
            # pixel((67, 10), (0xA1, 0x82, 0x47)),
            # pixel((75, 10), (0xB2, 0x8D, 0x51)),
            # pixel((80, 15), (0xBE, 0x97, 0x5B)),
            # pixel((58, 26), (0xE2, 0xDF, 0x86)),
            # pixel((68, 27), (0x8E, 0x63, 0x37)),
            # pixel((80, 27), (0x99, 0x73, 0x45)),
            # pixel((60, 34), (0xB4, 0x9D, 0x51)),
            # pixel((80, 34), (0x23, 0x1F, 0x20)),
        )
        self.slq = pixels(  # 升龙拳
            'r',
            pixel((109, 9), (0x1E, 0x09, 0x05)),
            pixel((116, 9), (0xC4, 0x99, 0x2B)),
            pixel((123, 9), (0xBF, 0x7E, 0x24)),
            pixel((130, 12), (0x1B, 0x08, 0x08)),
            pixel((130, 22), (0x2E, 0x0D, 0x0B)),
            pixel((122, 31), (0xD1, 0x9E, 0x45)),
            pixel((111, 28), (0xDF, 0xE4, 0x7C)),
            pixel((106, 16), (0x3A, 0x14, 0x0C)),
        )
        self.lhq = pixels(  # 炼火拳
            'c',
            pixel((158, 9), (0x31, 0x1C, 0x18)),
            pixel((166, 9), (0x95, 0x6A, 0x41)),
            pixel((173, 9), (0xC9, 0x95, 0x57)),
            pixel((179, 14), (0x69, 0x4F, 0x37)),
            pixel((182, 31), (0xAF, 0x81, 0x50)),
            pixel((169, 31), (0xD6, 0xA6, 0x63)),
            pixel((154, 28), (0xF8, 0xF3, 0xC8)),
            pixel((159, 17), (0xE1, 0xD3, 0x73)),

        )
        self.ldz = pixels(  # 裂地斩
            'v',
            pixel((212, 13), (0xED, 0xEA, 0x91)),
            pixel((217, 13), (0x49, 0x37, 0x28)),
            pixel((223, 14), (0xE9, 0xD9, 0x84)),
            pixel((227, 17), (0xD9, 0xA8, 0x67)),
            pixel((227, 26), (0xCB, 0xBB, 0x78)),
            pixel((221, 28), (0x61, 0x4A, 0x31)),
            pixel((212, 28), (0xCC, 0xB0, 0x71)),
            pixel((209, 22), (0xE9, 0xDD, 0x80)),
        )

    def match(self):
        while True:
            edged = ImageGrab.grab(self.region)

            if self.ql.match(edged) is False:
                if self.ldz.match(edged):
                    press(self.ldz.hotkey)
                    continue

            if self.ylpd.match(edged) is False:
                if self.slq.match(edged):
                    press(self.slq.hotkey)
                elif self.lhq.match(edged):
                    press(self.lhq.hotkey)

            time.sleep(0.2)

        # if self.ql.match(edged) is False:
        #     if self.ldz.match(edged):
        #         press(self.ldz.hotkey)
        #     else:
        #         if self.ylpd.match(edged) is False:
        #             if self.slq.match(edged):
        #                 press(self.slq.hotkey)
        #             elif self.lhq.match(edged):
        #                 press(self.lhq.hotkey)
        # else:
        #     if self.ylpd.match(edged) is False:
        #         if self.slq.match(edged):
        #             press(self.slq.hotkey)
        #         elif self.lhq.match(edged):
        #             press(self.lhq.hotkey)

        #


r = Region((965, 985, 965 + 243, 985 + 47))
r.match()
