
from context_manager import MyRaises

def test_raises():
  with MyRaises(ZeroDivisionError):
    2/0
  assert(True)

def test_no_raises():
  try:
    with MyRaises(IndexError):
      2/0
  except AssertionError:
    assert(True)
  else:
    assert(False)
