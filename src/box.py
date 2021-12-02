from src.point import Point


class Box:
    def __init__(self, a, b, c, d):
        self.a = Point(a)
        self.b = Point(b)
        self.c = Point(c)
        self.d = Point(d)

    def __str__(self):
        return "(" + str(self.a) + ", " + str(self.b) + ", " + str(self.c) + ", " + str(self.d) + ")"