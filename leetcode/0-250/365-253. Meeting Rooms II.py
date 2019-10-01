# 253. Meeting Rooms II
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        ans, heap = 0, []
        for s, e in sorted(intervals):
            while heap and heap[0] <= s:
                heapq.heappop(heap)
            heapq.heappush(heap, e)
            ans = max(ans, len(heap))
        return ans