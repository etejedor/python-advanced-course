
import sys
version = sys.argv[1]

from Particle import Particle

if version == 'pyglet':
    import pyglet
    from math import sin, cos, pi, sqrt
    twopi = 2*pi

    window = pyglet.window.Window(600,400)
    fps_display = pyglet.clock.ClockDisplay()

    p = Particle(60, (window.width / 2, window.height / 2), (80.0, 150.0))

    @window.event
    def on_draw():
        window.clear()
        def circle_vertices():
            delta_angle = twopi / 20
            angle = 0
            while angle < twopi:
                yield p.x + p.r * cos(angle)
                yield p.y + p.r * sin(angle)
                angle += delta_angle

        pyglet.gl.glColor3f(1.0, 1.0, 0)
        pyglet.graphics.draw(20, pyglet.gl.GL_LINE_LOOP,
                         ('v2f', tuple(circle_vertices())))

        fps_display.draw()


    def update(dt):
        global p
        p.move(dt)
        p.bounce((0, window.width, 0, window.height))

    pyglet.clock.schedule_interval(update, 1/60.0)

    pyglet.app.run()

else:

    import tkinter as tk

    master = tk.Tk()

    w = tk.Canvas(master, width=600, height=400, bg='black')
    w.pack()

    p = Particle(60, (w.winfo_height() / 2, w.winfo_width() / 2), (80.0,150.0))

    particle = w.create_oval(p.x,p.y, p.r,p.r, outline='yellow')

    def update(dt):
        global p
        oldx, oldy = p.x,p.y
        p.move(dt)
        p.bounce((0, w.winfo_width(), 0, w.winfo_height()))

        w.move(particle, p.x-oldx, p.y-oldy)
        w.update()
        w.after(17, update, 1/60.0)

    update(0)

    tk.mainloop()
