# 525. Contiguous Array
class Solution:
    # TLE
    def findMaxLength2(self, A) -> int:
        longest = 0
        n = len(A)

        for i in range(n):
            cnt = 0
            for j in range(i, n):
                cnt += 1 if A[j] else -1
                if cnt == 0:
                    longest = max(longest, j - i + 1)

        return longest

    # TLE
    def findMaxLength(self, nums) -> int:
        d = {}
        longest = 0
        
        for i, x in enumerate(nums):
            tmp = {}
            cur_k = 1 if x else -1
            for k, v in d.items():
                k += cur_k
                tmp[k] = min(tmp.get(k, float('inf')), v)
            tmp[cur_k] = min(tmp.get(cur_k, float('inf')), i)
            
            d = tmp.copy()
            if 0 in d:
                longest = max(longest, i - d[0] + 1)
        
        return longest
                
print(Solution().findMaxLength([1,0,1,1,0,0,0,0,1]))