from pytest import mark
parametrize = mark.parametrize

from secret import secret


from hypothesis import given, example
from hypothesis.strategies import integers

@given(integers(), integers())
@example(1,2)
def test_random(n, p):
    assert secret(n, p) == n+p

@parametrize('q1,q2,a', ( (1,2,3),
                          (0,7,7) ))
def test_first(q1, q2, a):
  assert secret(q1,q2) == a
