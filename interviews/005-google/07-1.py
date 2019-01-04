import heapq
from math import sqrt, ceil
import random
# solution 1: min heap
def solution(K, X, Y):
    dist = [getDistance(X[i], Y[i]) for i in range(len(X))]
    return ceil(sqrt(heapq.nsmallest(K, dist)[-1]))

def getDistance(x, y):
    return x**2 + y**2

print(solution(4, [-1,2,-4,2,4], [1,2,-4,2,-1]))
print(solution(4, [-1, 2, -4, 200, 4], [1, 2, -4, 200, -1]))
print(solution(4, [-1, 2, -4, 0, 4], [1, 2, -4, 0, -1]))
print(solution(4, [-1, 2, -4, 0, 4, 0], [1, 2, -4, 0, -1, 0]))
print(solution(1, [0], [0]))
print(solution(1, [10], [10]))
print(solution(1, [3], [4]))
print(solution(1, [-1, 2, -4, 2, 4], [1, 2, -4, 2, -1]))