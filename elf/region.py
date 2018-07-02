from PIL import ImageGrab


class Region(object):

    def __init__(self, area):
        super(Region, self).__init__()
        self.edged = ImageGrab.grab(area)

    def match(self, xy, pixel):
        """误差在 100 像素内
        """
        return abs(
            sum(self.edged.getpixel(pixel.xy)) - sum(pixel.rgb)
        ) <= 100
