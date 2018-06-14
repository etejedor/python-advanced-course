
import pyglet
from math import sin, cos, pi, sqrt
twopi = 2*pi

import tkinter as tk

class Display:

  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.particles = []

  def update(self, dt, boundaries):
    for p in self.particles:
      p.move(dt)
      p.bounce(boundaries)

  def add(self, p):
    self.particles.append(p)


class PygletDisplay(Display):
   
  def __init__(self, width, height):
    super().__init__(width, height)
    self._window = pyglet.window.Window(width, height)
    self._fps_display = pyglet.clock.ClockDisplay()

    @self._window.event
    def on_draw():
      self._window.clear()
      for p in self.particles:
        p.draw(self)
      self._fps_display.draw()

  def go(self):
    pyglet.clock.schedule_interval(self.update,
                                   1/60.0,
                                   (0, self.width, 0, self.height))
    pyglet.app.run()

  def draw_circle(self, x, y, r, c): 
    def circle_vertices():
      delta_angle = twopi / 20
      angle = 0
      while angle < twopi:
        yield x + r * cos(angle)
        yield y + r * sin(angle)
        angle += delta_angle

    #pyglet.gl.glColor3f(1.0, 1.0, 0)
    pyglet.gl.glColor3f(*c.as_rgb_01())
    pyglet.graphics.draw(20, pyglet.gl.GL_LINE_LOOP,
                         ('v2f', tuple(circle_vertices())))


class TkinterDisplay(Display):

  def __init__(self, width, height):
    super().__init__(width, height)

    master = tk.Tk()
    self._window = tk.Canvas(master, width=width, height=height, bg='black')
    self._window.pack()

  def update(self, dt, boundaries):
    super().update(dt, boundaries)
    self._window.delete(tk.ALL)

    for p in self.particles:
      p.draw(self)

    self._window.update()
    self._window.after(17, self.update, 1/60.0, (0, self.width, 0, self.height))

  def go(self):
    self.update(0, (0, self.width, 0, self.height))
    tk.mainloop()

  def draw_circle(self, x, y, r, c):
    self._window.create_oval(x-r, y-r, x+r, y+r, outline=str("#" + c.as_rgb_f()))
