
class Colour:

  f_to_n = { d:n for n,d in enumerate('0123456789abcdef') }
  n_to_f = { n:d for d,n in f_to_n.items() }

  @staticmethod
  def from_rgb_01(r, g, b):
    c = Colour()
    c._rgb = (r,g,b)
    return c

  def as_rgb_01(self):
    return self._rgb

  def as_rgb_f(self):
    return ''.join(self.n_to_f[int(v*15)] for v in self._rgb) 

  @classmethod
  def from_rgb_f(cls, rgb):
    c = cls()
    c._rgb = tuple(cls.f_to_n[d] / 15.0 for d in rgb.lower())
    return c

 
Color = Colour

name_to_rgb = {
   'BLACK'  : (0,0,0),
   'WHITE'  : (1,1,1),
   'RED'    : (1,0,0),
   'GREEN'  : (0,1,0),
   'BLUE'   : (0,0,1),
   'YELLOW' : (1,1,0),
   'CYAN'   : (0,1,1),
   'MAGENTA': (1,0,1)
}

# We cannot do it through getattr, it is only for instances
for key,value in name_to_rgb.items():
  setattr(Colour, key, Colour.from_rgb_01(*value))
