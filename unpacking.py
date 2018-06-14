
def fn(a,b,*boo):
  pass

def fn(a, b, **boo):
  pass
# Collect any remaining positional/keyword arguments into a tuple/dict and bind it to the name which follows the */**
# Argument == data, parameter == name

# Only Py3
a,b,*c,d,e = 'this is an example'


class Foo:
  def meth(*args):
    return args

  @staticmethod
  def static(*args):
    return args

  @classmethod
  def class_(*args):  # def class_(cls, *args):
    return args

Foo().meth()
Foo.meth()

def fn(*args):
  return args

# The binding behaviour happens in these two cases
Foo.banana = fn
Foo.haha = lambda *args: args

# The binding mechanism (reception of self) does not work here because dir is implemented with the Python C API
Foo.dir = dir

# Both are ok, no parameter is passed in any case
Foo().static()
Foo.static()

# This will get as first parameter the class
Foo().class_()
Foo.class_()
