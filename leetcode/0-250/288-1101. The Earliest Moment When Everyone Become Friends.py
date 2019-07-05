# 1101. The Earliest Moment When Everyone Become Friends
class Solution:
    def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        arr = [set([i]) for i in range(N)]
        logs.sort()
        
        for lg in logs:
            newfr = arr[lg[1]] | arr[lg[2]]
            if len(newfr) == N:
                return lg[0]
            for i in newfr:
                arr[i] = newfr
        
        return -1