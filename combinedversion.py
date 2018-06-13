
import sys
version = sys.argv[1]

from Particle import Particle
from Display import PygletDisplay, TkinterDisplay

width, height = 600, 400 

p = Particle(60, (width / 2, height / 2), (80.0, 150.0))

if version == 'pyglet':
    d = PygletDisplay(width, height, p)
else:
    d = TkinterDisplay(width, height, p)

d.go()
