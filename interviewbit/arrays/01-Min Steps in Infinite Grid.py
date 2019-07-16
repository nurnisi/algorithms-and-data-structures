# Min Steps in Infinite Grid
class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return an integer
	def coverPoints(self, A, B):
	    ans = 0
        for i in range(1, len(A)):
            a = abs(A[i] - A[i-1])
            b = abs(B[i] - B[i-1])
            ans += max(a, b)
        return ans