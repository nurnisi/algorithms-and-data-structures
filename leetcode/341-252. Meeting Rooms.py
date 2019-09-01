# 252. Meeting Rooms
import heapq
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        s = sorted([s for s, e in intervals])
        e = sorted([e for s, e in intervals])
        rooms = sp = ep = 0
        while sp < len(intervals):
            if s[sp] >= e[ep]:
                rooms -= 1
                ep += 1
            rooms += 1
            sp += 1
        return rooms <= 1

    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        rooms = []
        for s,e in sorted(intervals):
            if rooms and rooms[0] <= s:
                heapq.heappop(rooms)
            heapq.heappush(rooms, e)
        return len(rooms) <= 1        