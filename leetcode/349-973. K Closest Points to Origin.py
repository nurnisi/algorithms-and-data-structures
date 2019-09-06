# 973. K Closest Points to Origin
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heapq.heappush(heap, (x*x + y*y, (x,y)))
        
        return [heapq.heappop(heap)[1] for _ in range(K)]