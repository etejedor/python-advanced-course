
import sys
version = sys.argv[1]

from Particle import Particle
from Colour import Colour

if version == 'pyglet':
    from Display import PygletDisplay as Display
else:
    from Display import TkinterDisplay as Display

d = Display(600, 400)

d.add(Particle(60, (300, 200), (80.0, 150.0), Colour.BLUE))
d.add(Particle(20, (100, 100), (40.0, 100.0), Colour.RED))

d.go()
