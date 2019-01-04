import heapq
from math import sqrt, ceil
import random
# solution 1: min heap
def solution(K, X, Y):
    dist = [getDistance(X[i], Y[i]) for i in range(len(X))]
    return ceil(sqrt(heapq.nsmallest(K, dist)[-1]))

def getDistance(x, y):
    return x**2 + y**2

# solution 2: quick select
def solution(K, X, Y):
    dist = [getDistance(X[i], Y[i]) for i in range(len(X))]
    return ceil(sqrt(quickSelect(dist, K)))

def quickSelect(A, K):
    if len(A) == 1: return A[0]
    r = random.randint(0, len(A)-1)
    left, right = [], []
    for i in range(len(A)):
        if A[i] <= A[r]: left.append(A[i])
        else: right.append(A[i])
    
    if len(left) < K: 
        return quickSelect(right, K-len(left))
    else:
        return quickSelect(left, K)

print(solution(4, [-1,2,-4,2,4], [1,2,-4,2,-1]))
print(solution(4, [-1, 2, -4, 200, 4], [1, 2, -4, 200, -1]))
print(solution(4, [-1, 2, -4, 0, 4], [1, 2, -4, 0, -1]))
print(solution(4, [-1, 2, -4, 0, 4, 0], [1, 2, -4, 0, -1, 0]))
print(solution(1, [0], [0]))
print(solution(1, [10], [10]))
print(solution(1, [3], [4]))
print(solution(1, [-1, 2, -4, 2, 4], [1, 2, -4, 2, -1]))