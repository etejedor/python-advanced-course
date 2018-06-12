
from fib import fib_iter as fib

from pytest import mark
parametrize = mark.parametrize

from hypothesis            import given, example
from hypothesis.strategies import integers

@given(integers(min_value = 2, max_value = 10000))
@example(235)
def test_fib_equals_sum_of_previous(n):
  assert fib(n) == fib(n-1) + fib(n-2)

@parametrize('q,a', ((0,0),
                     (1,1),
                     (2,1),
                     (3,2),
                     (4,3),
                     (5,5)))
def test_fib_examples(q,a):
  assert fib(q) == a

def test_fib_of_one():
  assert fib(1) == 1 
