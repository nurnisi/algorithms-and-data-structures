# 1007. Minimum Domino Rotations For Equal Row
import collections
class Solution:
    def minDominoRotations(self, A, B) -> int:
        cnt_a = collections.Counter(A)
        cnt_b = collections.Counter(B)
        
        ans, n = float('inf'), len(A)
        for i in range(1, 7):
            if cnt_a.get(i, 0) + cnt_b.get(i, 0) >= n:
                ans_a = ans_b = 0
                flag = True
                for j in range(n):
                    if A[j] != i and B[j] == i:
                        ans_a += 1
                    if B[j] != i and A[j] == i:
                        ans_b += 1
                    
                    if A[j] != i and B[j] != i:
                        flag = False
                        break
                
                if flag:
                    ans = min(ans, ans_a, ans_b)
        
        return ans if ans != float('inf') else -1

print(Solution().minDominoRotations([6,1,6,4,6,6], [5,6,2,6,3,6]))
                