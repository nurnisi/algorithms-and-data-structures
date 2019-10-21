# 986. Interval List Intersections
class Solution:
    def intervalIntersection(self, A, B):
        m, n = len(A), len(B)
        i = j = 0
        ans = []
        while i < m and j < n:
            left = max(A[i][0], B[j][0])
            right = min(A[i][1], B[j][1])
            
            if left <= right: ans.append([left, right])
            
            if A[i][1] < B[j][1]: i += 1
            else: j += 1
        
        return ans