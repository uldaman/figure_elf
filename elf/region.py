import cv2
import numpy as np
from PIL import ImageGrab


def best_point(locations, precision):
    _, max_val, _, max_loc = cv2.minMaxLoc(locations)
    if max_val < precision:
        return None
    return max_loc


class RegionPixel(object):
    """绝对像素
    """

    def __init__(self, x, y, wight, heigh):
        super(RegionPixel, self).__init__()
        self.edged = ImageGrab.grab((x, y, x + wight, y + heigh))
        self.boundary = (wight, heigh)

    def match(self, pixels):
        """误差在 25 像素内
        """
        def __match(pixel):
            if pixel.xy[0] > self.boundary[0] or pixel.xy[1] > self.boundary[1]:
                return False
            rgb = self.edged.getpixel(pixel.xy)
            return all(
                (  # 生成一个迭代器，有短路效应
                    abs(rgb[0] - pixel.rgb[0]) <= 25,
                    abs(rgb[1] - pixel.rgb[1]) <= 25,
                    abs(rgb[2] - pixel.rgb[2]) <= 25
                )
            )
        return all(map(__match, pixels))


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
                x = pixel.xy[0] + first[1]
                y = pixel.xy[1] + first[0]
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


# ImageGrab.grab((7, 611, 7 + 80, 611 + 80)).save(r"C:\Users\HanXiao\Desktop\1.bmp")
