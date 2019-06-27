# 767. Reorganize String
import collections
import heapq
class Solution:
    def reorganizeString(self, S: str) -> str:
        heap = [[-v, k] for k, v in collections.Counter(S).items()]
        heapq.heapify(heap)
        ans = ""
        
        while len(heap) > 1:
            a, b = heapq.heappop(heap), heapq.heappop(heap)
            ans += (a[1] + b[1]) * -b[0]
            a[0] -= b[0]
            if a[0]: heapq.heappush(heap, a)
        
        if heap:
            if heap[0][0] < -1: return ""
            ans += heap[0][1]
        return ans

print(Solution().reorganizeString("vvvlo"))