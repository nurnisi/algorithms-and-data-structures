# 216. Combination Sum III
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def rec(sm, dg, i):
            if i == k and sm == n:
                ans.append(arr.copy())
            elif i < k and sm < n:
                for j in range(dg+1, 10):
                    arr.append(j)
                    rec(sm+j, j, i+1)
                    arr.pop()
        
        ans, arr = [], []
        rec(0, 0, 0)
        return ans
        
        