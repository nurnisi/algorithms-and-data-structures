# 973. K Closest Points to Origin
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = [(x*x + y*y, (x, y)) for x, y in points]
        heapq.heapify(heap)
        return [val[1] for val in heapq.nsmallest(K, heap)]
        
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return heapq.nsmallest(K, points, key=lambda p: p[0]*p[0]+p[1]*p[1])
        