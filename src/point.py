
class Point:
    def __init__(self, data):
        self.x = data[0][0][0][0]
        self.y = data[0][0][0][1]

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def as_tuple(self):
        return self.x, self.y
