# 922. Sort Array By Parity II
class Solution:
    def sortArrayByParityII(self, A):
        ans = A.copy()
        even, odd = 0, 1
        for i in A:
            if i % 2 == 0:
                ans[even] = i
                even += 2
            else:
                ans[odd] = i
                odd += 2
        
        return ans
        