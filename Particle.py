class Particle:

  def __init__(self, r, pos, vel):
    self.r = r
    self.x, self.y = pos
    self.vx, self.vy = vel

  def move(self, dt):
    self.x = self.x + dt * self.vx
    self.y = self.y + dt * self.vy

  def bounce(self, boundaries):
    xmin, xmax, ymin, ymax = boundaries
    if self.x + self.r > xmax:
      self.x = xmax - (2*self.r + (self.x - xmax))
      self.vx = - self.vx

    if self.x - self.r < xmin:
      self.x = xmin + (2*self.r + (xmin - self.x))
      self.vx = - self.vx

    if self.y + self.r > ymax:
      self.y = ymax - (2*self.r + (self.y - ymax))
      self.vy = - self.vy

    if self.y - self.r < ymin:
      self.y = ymin + (2*self.r + (ymin - self.y))
      self.vy = - self.vy

