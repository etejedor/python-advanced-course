from hypothesis import given
from hypothesis.strategies import integers

class Window:
  def __init__(self, x, y, w, h):
    self._x = x
    self._y = y
    self._w = w
    self._h = h

  def area(self):
    return self._w * self._h

  def perimeter(self):
    return 2 * (self._w + self._h)

  #@static # the class is hardcoded, only valid for Window
  #def from_corners(cls, x1, y1, x2, y2):
  #  return Window(x1,y1,x2-x1,y2-y1)

  @classmethod # inheritable polymorphic overloaded constructor - will invoke the real constructor of the class that is invoking it
  def from_corners(cls, x1, y1, x2, y2):
    return cls(x1,y1,x2-x1,y2-y1)


class BorderWindow(Window):
  border = 5
  def __init__(self, x, y, w, h):
    b = BorderWindow.border
    super().__init__(x-b,y-b,w+2*b,h+2*b)
 

def test_construct_corner_and_dimensions():
  x,y,w,h = 1,2,3,4
  Window(x,y,w,h)

def test_construct_two_corners():
  x1,y1,x2,y2 = 1,2,3,4
  w = Window.from_corners(x1, y1, x2, y2)
  assert w.area() == 4

winspec = (integers(), integers(), integers(min_value=1), integers(min_value=1))

@given(*winspec)
def test_area(x,y,w,h):
  win = Window(x,y,w,h)
  assert win.area() == w * h

@given(*winspec)
def test_perimeter(x,y,w,h):
  win = Window(x,y,w,h)
  assert win.perimeter() == 2 * (w + h)

def test_border_construct_corner_and_dimensions():                                                           
  x,y,w,h = 1,2,3,4                                                                                   
  BorderWindow(x,y,w,h)

def test_border_construct_two_corners():
  x1,y1,x2,y2 = 1,2,3,4
  win = BorderWindow.from_corners(x1, y1, x2, y2)
  w = x2 - x1
  h = y2 - y1
  assert win.area() == (w+10) * (h+10)

@given(*winspec)                                                                                      
def test_border_area(x,y,w,h):                                                                               
  win = BorderWindow(x,y,w,h)                                                                               
  assert win.area() == (w+10) * (h+10)
