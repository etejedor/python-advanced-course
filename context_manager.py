
class MyRaises:

  def __init__(self, exception):
    self._exception = exception

  def __enter__(self):
    pass

  def __exit__(self, extype, exception, tb):
    if extype == self._exception:
      return True
    raise AssertionError

