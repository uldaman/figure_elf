from PIL import ImageGrab


class Region(object):

    def __init__(self, x, y, wight, heigh):
        super(Region, self).__init__()
        self.edged = ImageGrab.grab((x, y, x + wight, y + heigh))

    def match(self, pixel):
        """误差在 100 像素内
        """
        return abs(
            sum(self.edged.getpixel(pixel.xy)) - sum(pixel.rgb)
        ) <= 100
