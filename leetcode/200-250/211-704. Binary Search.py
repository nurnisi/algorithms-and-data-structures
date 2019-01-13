# 704. Binary Search
class Solution:
    # iterative
    def search(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target: return mid
            elif nums[mid] < target: l = mid + 1
            else: r = mid
        return -1

sol = Solution()
print(sol.search(nums = [-1,0,3,5,9,12], target = 9))
print(sol.search(nums = [-1,0,3,5,9,12], target = 2))
print(sol.search([5], 5))
