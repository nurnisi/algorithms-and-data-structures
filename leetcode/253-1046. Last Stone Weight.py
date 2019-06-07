# 1046. Last Stone Weight
import heapq
class Solution:
    def lastStoneWeight(self, stones) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            heapq.heappush(stones, heapq.heappop(stones) - heapq.heappop(stones))

        return -stones[0]

print(Solution().lastStoneWeight([2,7,4,1,8,1]))