
from math import sqrt

class Vector:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __getitem__(self, idx):
    if idx == 0: return self.x
    elif idx == 1: return self.y

  def __setitem__(self, idx, item):
    if idx == 0: self.x = item
    elif idx == 1: self.y = item

  def __add__(self, vec):
    return Vector(self.x + vec.x, self.y + vec.y)

  def __sub__(self, vec):
    return Vector(self.x - vec.x, self.y - vec.y)

  def __neg__(self):
    return Vector(-self.x, -self.y)

  def __mul__(self, scalar):
    return Vector(self.x*scalar, self.y*scalar)

  def __rmul__(self, scalar):
    return self * scalar

  def __truediv__(self, scalar):
    return Vector(self.x/scalar, self.y/scalar)

  def __abs__(self):
    return sqrt(self.x*self.x + self.y*self.y)
