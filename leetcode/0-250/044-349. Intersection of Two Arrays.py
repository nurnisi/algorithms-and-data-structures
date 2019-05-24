# 349. Intersection of Two Arrays
class Solution:
    def intersection(self, nums1, nums2):
        s1, s2 = set(nums1), set(nums2)
        return [i for i in s2 if i in s1]