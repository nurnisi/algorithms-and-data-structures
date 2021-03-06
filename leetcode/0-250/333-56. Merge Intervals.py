# 56. Merge Intervals
import heapq
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

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for i in sorted(intervals):
            if merged and merged[-1][1] >= i[0]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged.append(i)
        return merged