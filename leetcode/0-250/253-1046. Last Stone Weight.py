# 1046. Last Stone Weight
import heapq
import bisect
class Solution:
    # heap
    def lastStoneWeight2(self, stones) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            heapq.heappush(stones, heapq.heappop(stones) - heapq.heappop(stones))

        return -stones[0]

    # bisect
    def lastStoneWeight(self, stones) -> int:
        stones = sorted(stones)
        for _ in range(len(stones) - 1):
            x, y = stones.pop(), stones.pop()
            bisect.insort(stones, abs(x - y))

        return stones.pop()

print(Solution().lastStoneWeight([2,7,4,1,8,1]))