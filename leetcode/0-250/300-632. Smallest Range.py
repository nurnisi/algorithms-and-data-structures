# 632. Smallest Range
import heapq
class Solution:
    def smallestRange(self, A):
        pq = [(row[0], i, 0) for i, row in enumerate(A)]
        heapq.heapify(pq)
        
        ans = -1e9, 1e9
        right = max(row[0] for row in A)
        while pq:
            left, i, j = heapq.heappop(pq)
            if right - left < ans[1] - ans[0]:
                ans = left, right
            if j + 1 == len(A[i]):
                return ans
            v = A[i][j+1]
            right = max(right, v)
            heapq.heappush(pq, (v, i, j+1))

print(Solution().smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]))