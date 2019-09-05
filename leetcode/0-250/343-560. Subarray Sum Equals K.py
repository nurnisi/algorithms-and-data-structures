# 560. Subarray Sum Equals K
import collections
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = collections.defaultdict(int)
        d[0] += 1
        ans = cursum = 0
        for x in nums:
            cursum += x
            ans += d[cursum-k]
            d[cursum] += 1
        
        return ans