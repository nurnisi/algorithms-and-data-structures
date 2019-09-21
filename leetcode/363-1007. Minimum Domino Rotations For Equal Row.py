# 1007. Minimum Domino Rotations For Equal Row
import collections
class Solution:
    def minDominoRotations2(self, A, B) -> int:
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

    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        swaps_a = [[i, 0] for i in range(1,7)]
        swaps_b = [[i, 0] for i in range(1,7)]
        
        for i in range(len(A)):
            if not swaps_a and not swaps_b:
                return -1
            
            for j in range(len(swaps_a)-1, -1, -1):
                if swaps_a[j][0] == A[i]:
                    continue
                elif swaps_a[j][0] == B[i]:
                    swaps_a[j][1] += 1
                else:
                    swaps_a.pop(j)
            
            for j in range(len(swaps_b)-1, -1, -1):
                if swaps_b[j][0] == B[i]:
                    continue
                elif swaps_b[j][0] == A[i]:
                    swaps_b[j][1] += 1
                else:
                    swaps_b.pop(j)
            
                    
        return min(sw for v, sw in swaps_a+swaps_b)

print(Solution().minDominoRotations([6,1,6,4,6,6], [5,6,2,6,3,6]))
                