# 189. Rotate Array
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        if n == 1 or k == 0 or k == n: return
        temp = nums[-k:]
        for i in range(n-k-1, -1, -1):
            nums[i+k] = nums[i]
        
        nums[:k] = temp

nums = [1,2,3,4,5,6,7]
sol = Solution()
sol.rotate(nums, 3)
print(nums)