# 1010. Pairs of Songs With Total Durations Divisible by 60
import collections
class Solution:
    def numPairsDivisibleBy60(self, time) -> int:
        arr = [0] * 60
        for t in time:
            arr[t % 60] += 1
        
        def fact(n):
            if n == 1: return 1
            return n + fact(n - 1)
        
        ans = 0
        if arr[0] > 1: ans += fact(arr[0] - 1)
        if arr[30] > 1: ans += fact(arr[30] - 1)
        
        for i in range(1, 30):
            ans += arr[60 - i] * arr[i]
                
        return ans
                
print(Solution().numPairsDivisibleBy60([15,63,451,213,37,209,343,319]))
print(Solution().numPairsDivisibleBy60([30,20,150,100,40]))
print(Solution().numPairsDivisibleBy60([60,60,60,60]))
