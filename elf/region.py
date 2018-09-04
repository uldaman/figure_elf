import cv2
import numpy as np
from PIL import ImageGrab


def best_point(locations, precision):
    _, max_val, _, max_loc = cv2.minMaxLoc(locations)
    if max_val < precision:
        return None
    return max_loc


class RegionRelativePixel(object):
    """相对像素
    """

    def __init__(self, x, y, wight, heigh):
        super(RegionRelativePixel, self).__init__()
        self.edged = np.array(ImageGrab.grab((x, y, x + wight, y + heigh)))
        self.boundary = (wight, heigh)

    def match(self, pixels):
        def _multi_match(first):
            """多点匹配
            """
            def _pixel_macth(pixel):
                """像素匹配
                """
                # np.array 转换后与笛卡尔（x，y）坐标相反，即 (y,x) = (x,y)
                x = first[1] + pixel.xy[0]
                y = first[0] + pixel.xy[1]
                if x > self.boundary[0] or y > self.boundary[1]:
                    return False
                return all(
                    (  # 生成一个迭代器，有短路效应
                       # np.array 转换后与笛卡尔（x，y）坐标相反，即 (y,x) = (x,y)
                        abs(self.edged[y, x][0] - pixel.rgb[0]) <= 25,
                        abs(self.edged[y, x][1] - pixel.rgb[1]) <= 25,
                        abs(self.edged[y, x][2] - pixel.rgb[2]) <= 25
                    )
                )
            return all(map(_pixel_macth, pixels[1:]))
        return any(map(_multi_match, np.argwhere((self.edged == pixels[0].rgb).all(-1))))


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


# ImageGrab.grab((1011, 985, 1015 + 96, 985 + 47)).save(r"C:\Users\HanXiao\Desktop\q.bmp")

# import time
# i = 100000
# while True:
#     time.sleep(10)
#     ImageGrab.grab((793, 943, 793 + 66, 943 + 66)).save(r"C:\Users\HanXiao\Desktop\{}.bmp".format(i))
#     i = i + 1
