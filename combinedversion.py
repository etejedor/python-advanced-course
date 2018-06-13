
import sys
version = sys.argv[1]


if version == 'pyglet':
    import pyglet
    from math import sin, cos, pi, sqrt
    twopi = 2*pi

    window = pyglet.window.Window(600,400)
    fps_display = pyglet.clock.ClockDisplay()

    x,y = window.width / 2, window.height / 2
    vx, vy = 80.0, 150.0
    x2,y2 = 30,60

    @window.event
    def on_draw():
        window.clear()
        def circle_vertices():
            delta_angle = twopi / 20
            angle = 0
            while angle < twopi:
                yield x + x2 * cos(angle)
                yield y + y2 * sin(angle)
                angle += delta_angle

        pyglet.gl.glColor3f(1.0, 1.0, 0)
        pyglet.graphics.draw(20, pyglet.gl.GL_LINE_LOOP,
                         ('v2f', tuple(circle_vertices())))

        fps_display.draw()


    def update(dt):
        global x,y, vx, vy, x2, y2
        x += vx*dt
        y += vy*dt

        if x + x2 > window.width:
            x = window.width - x2
            vx = - vx

        if x - x2 < 0:
            x =  x2
            vx = - vx

        if y + y2 > window.height:
            y = window.height - y2
            vy = - vy

        if y - y2 < 0:
            y = y2
            vy = - vy

    pyglet.clock.schedule_interval(update, 1/60.0)

    pyglet.app.run()

else:

    import tkinter as tk

    master = tk.Tk()

    w = tk.Canvas(master, width=600, height=400, bg='black')
    w.pack()

    x,y = w.winfo_height() / 2, w.winfo_width() / 2
    vx, vy = 80.0, 150.0

    x2, y2 = 60, 30
    particle = w.create_oval(x,y, x2,y2, outline='yellow')

    def update(dt):
        global x,y, vx, vy
        oldx, oldy = x,y
        x += vx*dt
        y += vy*dt

        if x + x2 > w.winfo_width():
            x = w.winfo_width() - x2
            vx = - vx

        if x < 0:
            x = 0
            vx = - vx

        if y + y2 > w.winfo_height():
            y = w.winfo_height() - y2
            vy = - vy

        if y < 0:
            y = 0
            vy = - vy

        w.move(particle, x-oldx, y-oldy)
        w.update()
        w.after(17, update, 1/60.0)

    update(0)

    tk.mainloop()
