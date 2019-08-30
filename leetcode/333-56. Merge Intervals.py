# 56. Merge Intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return intervals
        intervals.sort()
        start = intervals[0][0]
        ans, heap = [], [-intervals[0][1]]
        for intr in intervals:
            if -heap[0] < intr[0]:
                ans.append([start, -heap[0]])
                heap = [-intr[1]]
                start = intr[0]
            else:
                heapq.heappush(heap, -intr[1])
        
        ans.append([start, -heap[0]])
        return ans