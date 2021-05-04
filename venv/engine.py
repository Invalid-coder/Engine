import math


class Point:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, v):
        return Point(self.x + v.x, self.y + v.y, self.z + v.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)


class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, v):
        return Vector(self.x + v.x, self.y + v.y, self.z + v.z)

    def __sub__(self, other):
        return Vector(self.x - v.x, self.y - v.y, self.z - v.z)

    def __mul__(self, s):
        return Vector(self.x * s, self.y * s, self.z * s)

    def __truediv__(self, s):
        return Vector(self.x / s, self.y / s, self.z / s)

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def length_sqr(self):
        return self.x * self.x + self.y * self.y + self.z * self.z

    def normalized(self):
        return self / self.length()


def dot_product(a, b):
    return a.x * b.x + a.y * b.y + a.z * b.z


def approach(player, dt):
    """Jumping and gravity"""

    #dt = currTime - prevTime
    player.pos = player.pos + player.vel * dt
    palyer.vel = player.vel + player.gravity * dt


if __name__ == '__main__':
    v = Vector(2, 2)