# 33. Search in Rotated Sorted Array
class Solution:
    def search(self, nums, target: int) -> int:
        def binSearchPiv(l, r, target):
            while l < r:
                m = (l+r)//2
                if nums[m] > nums[m+1]: return m
                if nums[m] > target: l = m+1
                else: r = m
            return -1
        
        def binSearch(l, r, target):
            while l < r:
                m = (l+r)//2
                if nums[m] == target: return m
                if nums[m] < target: l = m+1
                else: r = m
            return -1
            
        n = len(nums)
        if nums and nums[0] > nums[n-1]:
            piv = binSearchPiv(0, n-1, nums[0])
            left, right = binSearch(0, piv+1, target), binSearch(piv+1, n, target)
            return left if left != -1 else right
        return binSearch(0, n, target)