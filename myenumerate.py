
l = ['a','b','c']

### ORIGINAL
for i,e in enumerate(l):
  print(i, e)


### CLASS
class ClassEnumerate:

  def __init__(self, iterable, start = 0):
    self._idx = start
    self._it = iter(iterable)
 
  def __iter__(self):
    return self
 
  def next(self, *sentinel):
    res = self._idx, next(self._it, *sentinel)
    self._idx += 1
    return res

  __next__ = next # Compatibility Py2 Py3

for i,e in ClassEnumerate(l):
  print(i, e)


### GENERATOR
def enumerate_generator(iterable, start = 0):
  idx = start
  for elem in iterable:
    yield idx, elem
    idx += 1 

for i,e in enumerate_generator(l):
  print(i,e)


### ITERTOOLS
from itertools import izip, count

# zip is only lazy in Py3, izip is lazy in both
def enumerate_itertools(iterable, start = 0):
  return izip(count(start), iterable)

for i,e in enumerate_itertools(l):
  print(i,e) 
