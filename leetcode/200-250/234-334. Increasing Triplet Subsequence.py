# 334. Increasing Triplet Subsequence
class Solution:
    def increasingTriplet(self, nums):
        first = second = float('inf')
        for n in nums:
            if n <= first: first = n
            elif n <= second: second = n
            else: return True
        return False

sol = Solution()
print(sol.increasingTriplet([1,7,3,0,1]))