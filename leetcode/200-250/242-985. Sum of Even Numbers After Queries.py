# 985. Sum of Even Numbers After Queries
class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        evens = sum(x for x in A if not x % 2)
        out = []
        for q in queries:
            if A[q[1]] % 2:
                if q[0] % 2: evens += A[q[1]] + q[0]
            else:
                if q[0] % 2: evens -= A[q[1]]
                else: evens += q[0]
            out.append(evens)
            A[q[1]] += q[0]
        return out

sol = Solution()
print(sol.sumEvenAfterQueries(A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]))
        