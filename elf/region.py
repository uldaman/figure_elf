import cv2
import numpy as np
from PIL import ImageGrab


def best_point(locations, precision):
    _, max_val, _, max_loc = cv2.minMaxLoc(locations)
    if max_val < precision:
        return None
    return max_loc


class RegionPixel(object):

    def __init__(self, x, y, wight, heigh):
        super(RegionPixel, self).__init__()
        self.edged = ImageGrab.grab((x, y, x + wight, y + heigh))

    def match(self, pixels):
        """误差在 25 像素内
        """
        def __match(pixel):
            rgb = self.edged.getpixel(pixel.xy)
            return all(
                (  # 生成一个迭代器
                    abs(rgb[0] - pixel.rgb[0]) <= 25,
                    abs(rgb[1] - pixel.rgb[1]) <= 25,
                    abs(rgb[2] - pixel.rgb[2]) <= 25
                )
            )
        return all(map(__match, pixels))


class RegionImage(object):

    def __init__(self, x, y, wight, heigh):
        super(RegionImage, self).__init__()
        self.edged = cv2.cvtColor(np.array(ImageGrab.grab((x, y, x + wight, y + heigh))), cv2.COLOR_RGB2GRAY)

    def match(self, template, precision=0.9):
        locations = cv2.matchTemplate(self.edged, template, cv2.TM_CCOEFF_NORMED)
        return best_point(locations, precision)


class RegionImageByMask(object):

    def __init__(self, x, y, wight, heigh):
        super(RegionImage, self).__init__()
        self.edged = cv2.cvtColor(np.array(ImageGrab.grab((x, y, x + wight, y + heigh))), cv2.COLOR_RGB2BGR)

    def match(self, template, mask, precision=0.9):
        locations = cv2.matchTemplate(self.edged, template, cv2.TM_CCORR_NORMED, mask=mask)
        return best_point(locations, precision)


# ImageGrab.grab((965, 985, 965 + 243, 985 + 47)).save(r"C:\Users\HanXiao\Desktop\1.bmp")
