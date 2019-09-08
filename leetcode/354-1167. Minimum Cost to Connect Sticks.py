# 1167. Minimum Cost to Connect Sticks
import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        cost = 0
        
        while len(sticks) > 1:
            cur = heapq.heappop(sticks) + heapq.heappop(sticks)
            cost += cur
            heapq.heappush(sticks, cur)
            
        return cost