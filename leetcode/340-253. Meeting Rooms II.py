# 253. Meeting Rooms II
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        rooms = 0
        for start, end in sorted(intervals):
            while heap and heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
            rooms = max(rooms, len(heap))
        return rooms

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        for start, end in sorted(intervals):
            if heap and heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
        return len(heap)