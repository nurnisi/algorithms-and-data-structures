# Root of Number
def root(x, n):
  return binary_search(1, x, x, n) # log(x)

def binary_search(l, r, x, n):
  while l < r:
    m = (l + r) / 2.0
    cur = pow(m, n)
    print(cur)
    if abs(x - cur) < 0.001:
      return m
    elif x > cur:
      l = m
    else:
      r = m
      
  return -1