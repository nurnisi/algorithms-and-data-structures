# 215. Kth Largest Element in an Array
import heapq
import random
class Solution:
    # sorting
    def findKthLargest2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        arr = nums.copy()
        arr.sort()
        
        return arr[-k]

    # max heap
    def findKthLargest3(self, nums, k):
        arr = [-num for num in nums]
        heapq.heapify(arr)
        for _ in range(k-1):
            heapq.heappop(arr)
        return -heapq.heappop(arr)

    # heap: Leetcode solution
    def findKthLargest4(self, nums, k):
        return heapq.nlargest(k, nums)[-1]

    # quick select: Leetcode solution
    def findKthLargest4(self, nums, k):
        def partition(i, j, pivotIndex):
            pivot = nums[pivotIndex]
            nums[pivotIndex], nums[j] = nums[j], nums[pivotIndex]
            storeIndex = i
            for x in range(i, j):
                if nums[x] < pivot:
                    nums[x], nums[storeIndex] = nums[storeIndex], nums[x]
                    storeIndex += 1
            
            nums[storeIndex], nums[j] = nums[j], nums[storeIndex]
            return storeIndex
        
        def select(i, j, k_smallest):
            if i == j: return nums[i]
            pivotIndex = random.randint(i, j)
            pivotIndex = partition(i, j, pivotIndex)

            if k_smallest == pivotIndex: return nums[k_smallest]
            elif k_smallest < pivotIndex: return select(i, pivotIndex - 1, k_smallest)
            else: return select(pivotIndex + 1, j, k_smallest)

        select(0, len(nums) - 1, len(nums) - k)
        return nums[len(nums) - k]

sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4,3], 2))