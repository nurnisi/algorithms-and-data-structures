# 975. Odd Even Jump
class Solution:
    # TLE
    def oddEvenJumps(self, A):
        n = len(A)
        jumps = [[False, False] for _ in A]
        jumps[n-1] = [True, True]
        
        cnt = 1
        for i in range(n-2, -1, -1):
            fl_odd = list(filter(lambda x: A[i] <= x, A[i+1:]))
            if fl_odd:
                odd = A[i+1:].index(min(fl_odd)) + i+1
                jumps[i][0] = jumps[odd][1]    
            
            fl_even = list(filter(lambda x: A[i] >= x, A[i+1:]))
            if fl_even:
                even = A[i+1:].index(max(fl_even)) + i+1
                jumps[i][1] = jumps[even][0]
            
            cnt += 1 if jumps[i][0] else 0
        
        return cnt

A = [10,13,12,14,15]
print(Solution().oddEvenJumps(A))