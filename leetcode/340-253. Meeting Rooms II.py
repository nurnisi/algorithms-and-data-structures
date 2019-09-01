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

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        sSort, eSort = sorted([s for s,e in intervals]), sorted([e for s,e in intervals])
        rooms = sptr = eptr = 0
        while sptr < len(intervals):
            if sSort[sptr] >= eSort[eptr]:
                rooms, eptr = rooms-1, eptr+1
            rooms, sptr = rooms+1, sptr+1
        return rooms
        