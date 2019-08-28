# 581. Shortest Unsorted Continuous Subarray
class Solution:
    def findUnsortedSubarray2(self, nums) -> int:
        nums_sorted = sorted(nums)
        n = len(nums)
        i, j = -1, n
        while i < n-1 and nums[i+1] == nums_sorted[i+1]:
            i += 1
        while j > 0 and nums[j-1] == nums_sorted[j-1]:
            j -= 1
        return 0 if i == n-1 else j-i-1

    def findUnsortedSubarray(self, nums) -> int:
        l, r = 0, len(nums)-1
        while l < r and nums[l] <= nums[l+1]: 
            l += 1
        
        if l >= r: 
            return 0
        
        while nums[r-1] <= nums[r]: 
            r -= 1
        
        mini, maxi = min(nums[l:r+1]), max(nums[l:r+1])
        
        while l >= 0 and nums[l] > mini: 
            l -= 1
            
        while r < len(nums) and nums[r] < maxi:
            r += 1
        
        return r - l - 1
        
        

print(Solution().findUnsortedSubarray([1,3,2,4,5]))