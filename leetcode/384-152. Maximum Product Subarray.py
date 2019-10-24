# 152. Maximum Product Subarray
class Solution:
    # TLE
    def maxProduct(self, nums: List[int]) -> int:
        arrs = []
        if 0 in nums:
            i = prev = 0
            while i <= len(nums):
                if i == len(nums) or nums[i] == 0:
                    arrs.append(nums[prev:i])
                    prev = i + 1
                i += 1
            arrs.append([0])
        else:
            arrs.append(nums)
                    
        def helper(arr):
            preProd = [1]
            for x in arr:
                preProd.append(preProd[-1] * x)

            ans = float('-inf')
            for i in range(len(preProd)):
                for j in range(i+1, len(preProd)):
                        ans = max(ans, preProd[j] // preProd[i])

            return ans
        
        return max([helper(a) for a in arrs])