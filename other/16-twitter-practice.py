import collections
def partion_array(A, n, k):
    return n % k == 0 and all(val <= n // k for key, val in collections.Counter(A).items())

print(partion_array([1,2,2,2], 4, 2))