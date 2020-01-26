class Counter:
  def __init__(self, start, step=1):
    self.start = start
    self.current = start
    self.step = step

  def next(self):
    self.current += self.step
    return self.current
