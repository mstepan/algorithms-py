import math


class Point:

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __to_polar(self):
        r = math.sqrt(self.x*self.x + self.y*self.y)
        angle = math.degrees(math.atan2(self.y, self.x))
        if angle < 0:
            angle += 360
        return r, angle

    def __str__(self):
        r, angle = self.__to_polar()
        return "%s, (%s, %s), polar: (%.1F, %.1F)" % (self.name, self.x, self.y, r, angle)

    __repr__ = __str__
