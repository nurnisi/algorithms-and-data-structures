# 4. Median of Two Sorted Arrays
class Solution:
    def findMedianSortedArrays2(self, nums1, nums2) -> float:
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

class Solution:
    def findMedianSortedArrays(self, X: List[int], Y: List[int]) -> float:
        if len(X) > len(Y): 
            return self.findMedianSortedArrays(Y, X)
        x, y = len(X), len(Y)
        l, r = 0, x
        
        while True:
            pX = (l + r) // 2
            pY = (x + y + 1) // 2 - pX
            
            lX = X[pX - 1] if pX - 1 >= 0 else float('-inf')
            rX = X[pX] if pX < x else float('inf')
            lY = Y[pY - 1] if pY - 1 >= 0 else float('-inf')
            rY = Y[pY] if pY < y else float('inf')
            
            if lX <= rY and lY <= rX:
                break    
            elif lX > rY:
                r = pX
            else:
                l = pX + 1
                
                
        if (x + y) % 2 == 0:
            return (max(lX, lY) + min(rX, rY)) / 2
        return max(lX, lY)