
from functools import wraps

def WRAPS(f_being_decorated):
  def decorator(its_proxy):
    its_proxy.__name__ = f_being_decorated.__name__
    its_proxy.__doc__ = f_being_decorated.__doc__
    its_proxy.__wrapped__ = f_being_decorated
    # and other attributes
    return its_proxy
  return decorator

def report_args(f):
  @WRAPS(f)
  def proxy(*args, **kwds):
    print(*args, **kwds)
    return f(*args, **kwds)
  return proxy

def report_result(f):
  @wraps(f)  # It gets us the metadata of the original object (e.g. documentation, name, etc.)
  def proxy(*args, **kwds):
    res = f(*args, **kwds)
    print(res)
    return res
  return proxy

def inc_result_by(inc): # this level collects the parameter
  def decorator(f): # this level is the decorator itself
    def proxy(*args, **kwds): # this level is a wrapper of the original function
      return f(*args, **kwds) + inc
    return proxy
  return decorator

@inc_result_by(10)
@report_result
@report_args
def badd(a,b):
  "***ed up addition"
  return a*b

report_all = lambda fn: report_args(report_result(fn))

print(badd(3,2))
#help(badd)



def uno(_):
  return 1

def inc(n):
  return n + 1

def add(n,m):
  return n+m

def inc_by(n):
  def inc(m):
    return n+m
  return inc

class INC_BY:
  def __init__(self,n):
    self.n = n
  def __call__(self,n):
    return self.n + n


def my_partial(fn, *args, **kwds):
  def proxy(*args2, **kwds2):
    return fn(*args, *args2, **kwds, **kwds2)
  return proxy

from functools import partial

@my_partial(add, 100)
@partial(add, 20)
@INC_BY(10)
@inc_by(10)
@inc
@uno
def hola():
  print('Hello')
