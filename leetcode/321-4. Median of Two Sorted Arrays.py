# 4. Median of Two Sorted Arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = []
        i = j = 0
        n1, n2 = len(nums1), len(nums2)
        
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                merge.append(nums1[i])
                i += 1
            else:
                merge.append(nums2[j])
                j += 1
        
        merge += nums1[i:]
        merge += nums2[j:]
        
        l = n1 + n2
        if l % 2 == 0:
            return (merge[l//2-1] + merge[l//2]) / 2
        return merge[l//2]