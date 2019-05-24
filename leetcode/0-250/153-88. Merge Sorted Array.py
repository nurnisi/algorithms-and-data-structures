# 88. Merge Sorted Array
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = m + n -1
        while m-1 >= 0 and n-1 >= 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[i] = nums1[m-1]
                m -= 1
            else:
                nums1[i] = nums2[n-1]
                n -= 1
            i -= 1

        while n-1 >= 0:
            nums1[i] = nums2[n-1]
            n -= 1
            i -= 1