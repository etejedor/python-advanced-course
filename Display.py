
import pyglet
from math import sin, cos, pi, sqrt

import tkinter as tk

class Display:

  def __init__(self, width, height, p):
    self.width = width
    self.height = height
    self.p = p

  def update(self, dt, boundaries):
    self.p.move(dt)
    self.p.bounce(boundaries)


class PygletDisplay(Display):
   
  def __init__(self, width, height, p):
    super().__init__(width, height, p)
    self._window = pyglet.window.Window(width,400)
    self._fps_display = pyglet.clock.ClockDisplay()
    pyglet.clock.schedule_interval(self.update,
                                   1/60.0,
                                   (0, width, 0, height))

    @self._window.event
    def on_draw():
      twopi = 2*pi
      self._window.clear()
      def circle_vertices():
        delta_angle = twopi / 20
        angle = 0
        while angle < twopi:
          yield self.p.x + self.p.r * cos(angle)
          yield self.p.y + self.p.r * sin(angle)
          angle += delta_angle

      pyglet.gl.glColor3f(1.0, 1.0, 0)
      pyglet.graphics.draw(20, pyglet.gl.GL_LINE_LOOP,
                        ('v2f', tuple(circle_vertices())))

      self._fps_display.draw()

  def go(self):
    pyglet.app.run()


class TkinterDisplay(Display):

  def __init__(self, width, height, p):
    super().__init__(width, height, p)

    master = tk.Tk()
    self._window = tk.Canvas(master, width=width, height=height, bg='black')
    self._window.pack()
    particle = self._window.create_oval(p.x,p.y, p.r, p.r, outline='yellow')
    self.update(0, (0, width, 0, height))

  def update(self, dt, boundaries):
    super().update(dt, boundaries)
    self._window.delete(tk.ALL)
    particle = self._window.create_oval(self.p.x-self.p.r,self.p.y-self.p.r, self.p.x+self.p.r, self.p.y+self.p.r, outline='yellow')
    self._window.update()
    self._window.after(17, self.update, 1/60.0, (0, self.width, 0, self.height))

  def go(self):
    tk.mainloop()

