# 215. Kth Largest Element in an Array
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        arr = nums.copy()
        arr.sort()
        
        return arr[-k]