from PIL import ImageGrab


class Region(object):

    def __init__(self, x, y, wight, heigh):
        super(Region, self).__init__()
        self.edged = ImageGrab.grab((x, y, x + wight, y + heigh))

    def match(self, pixel):
        """误差在 25 像素内
        """
        rgb = self.edged.getpixel(pixel.xy)
        return all(
            (  # 生成一个迭代器
                abs(rgb[0] - pixel.rgb[0]) <= 25,
                abs(rgb[1] - pixel.rgb[1]) <= 25,
                abs(rgb[2] - pixel.rgb[2]) <= 25
            )
        )
