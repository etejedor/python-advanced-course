
# usable many times, but not usual to store and reuse context managers
class MyRaises:

  def __init__(self, exception):
    self._exception = exception

  def __enter__(self):
    pass

  def __exit__(self, extype, exception, tb):
    if extype == self._exception:
      return True
    raise AssertionError


from contextlib import contextmanager

# only usable one time and it is exhausted (common case)
@contextmanager
def MyRaises_generator(exception):
    try:
      yield # runs the body of the context - if we return something (a), it comes out of "with cm(...) as a"
    except exception:
      assert True # We can write here just pass, we have to write something that does not raise an exception
    except:
      assert False # raises AssertionError
    else:
      assert False
     
