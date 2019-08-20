# 769. Max Chunks To Make Sorted
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        cnt = mx = 0
        for i in range(len(arr)):
            mx = max(mx, arr[i])
            if mx == i: 
                cnt += 1
        return cnt