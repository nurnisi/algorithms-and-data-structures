# 215. Kth Largest Element in an Array
import heapq
class Solution:
    # sorting
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        arr = nums.copy()
        arr.sort()
        
        return arr[-k]

    # max heap
    def findKthLargest2(self, nums, k):
        arr = [-num for num in nums]
        heapq.heapify(arr)
        for _ in range(k-1):
            heapq.heappop(arr)
        return -heapq.heappop(arr)

    # heap: Leetcode solution
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]

sol = Solution()
print(sol.findKthLargest2([3,2,1,5,6,4,3], 2))