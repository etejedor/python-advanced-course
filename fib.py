def fib_rec(n):
  if n < 2:
    return n
  return fib(n-1) + fib(n-2)

def fib_iter(n):
  if n < 2:
    return n

  n1, n2 = 1,0
  for _ in range(2, n):
    n1, n2 = n1+n2, n1

  return n1+n2
