# 989. Add to Array-Form of Integer
class Solution:
    def addToArrayForm2(self, A, K: int):
        i = len(A) - 1
        c = 0
        while i >= 0 and K > 0:
            A[i] += K % 10 + c
            c = A[i] // 10
            K //= 10
            A[i] %= 10
            i -= 1
            
        while K > 0:
            A.insert(0, K % 10 + c)
            c = A[0] // 10
            K //= 10
            A[0] %= 10
            
        while c > 0:
            if i >= 0:
                A[i] += c
                c = A[i] // 10
                A[i] %= 10
                i -= 1
            else:
                A.insert(0, c)
                c //= 10
                
        return A

    def addToArrayForm(self, A, K: int):
        A[-1] += K
        for i in range(len(A)-1, -1, -1):
            carry, A[i] = divmod(A[i], 10)
            if i: A[i-1] += carry
        if carry:
            A = list(map(int, str(carry))) + A

        return A

print(Solution().addToArrayForm([7], 993))