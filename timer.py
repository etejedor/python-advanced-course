
from time import time

from contextlib import contextmanager

class MyTime:
  pass

@contextmanager
def timer():
  t = MyTime()
  t1 = time()
  yield t
  t2 = time()
  t.time = t2 - t1
