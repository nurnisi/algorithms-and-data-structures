# 1094. Car Pooling
import heapq

class Solution:
    def carPooling(self, trips, capacity: int) -> bool:
        minheap = [(a[1], a) for a in trips]
        heapq.heapify(minheap)
        maxheap = []

        while minheap:
            curmin = heapq.heappop(minheap)
            capacity -= curmin[1][0]
            maxitem = (curmin[1][2], curmin[1])
            heapq.heappush(maxheap, maxitem)
            while maxheap and maxheap[0][0] <= curmin[0]:
                curmax = heapq.heappop(maxheap)
                capacity += curmax[1][0]
            if capacity < 0:
                return False
                
        return True
    
# print(Solution().carPooling([[2,1,5],[3,3,7]], capacity = 4))
# print(Solution().carPooling([[2,1,5],[3,3,7]], capacity = 5))
# print(Solution().carPooling([[2,1,5],[3,5,7]], capacity = 3))
print(Solution().carPooling([[3,2,8],[4,4,6],[10,8,9]], 11))
