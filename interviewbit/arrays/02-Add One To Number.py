# Add One To Number
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        c, i = 1, len(A)-1
        while i >= 0 and c != 0:
            A[i] += c
            c = A[i]//10
            A[i] %= 10
            i -= 1
            
        if c: A = [c] + A
        i = 0
        while A[i] == 0: i += 1
        
        return A[i:]