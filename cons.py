
class Cons:

  def __init__(self, item, tail=None):
    self.item = item
    self.tail = tail

  def __getitem__(self, pos):
    if pos == 0:
      return self.item
    if self.tail is None:
      raise IndexError
    return self.tail[pos-1]

  def __len__(self):
    if self.tail is None:
      return 1
    return 1 + len(self.tail)

  def __iter__(self): # Every time we call this function if will return a new generator (iterator)
    cons = self
    while cons is not None:
      yield cons.item  # Having a yield in a function means the function will return a generator when called
      cons = cons.tail

# We do not need the class below anymore
# Having the iterator as a separate class makes it possible to have two iterator objects that
# are independent
# If we implement __next__ in the Cons class, multiple iterators will depend on each other
class ConsIterator:

  def __init__(self, cons):
    self._cons = cons

  def __iter__(self):
    return self

  def __next__(self):
    if self._cons is None:
      raise StopIteration

    item = self._cons.item
    self._cons = self._cons.tail
    return item
