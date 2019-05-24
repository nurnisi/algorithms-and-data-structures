# 378. Kth Smallest Element in a Sorted Matrix
import heapq
from queue import PriorityQueue
class Solution:
    # priority queue
    def kthSmallest4(self, matrix, k):
        pq = PriorityQueue()
        n = len(matrix)

        for c in range(n):
            pq.put((matrix[0][c], 0, c))
      
        for i in range(k-1):
            val, r, c = pq.get()
            if r == n-1: continue
            pq.put((matrix[r+1][c], r+1, c))
        
        return pq.get()[0]

    # min heap
    def kthSmallest3(self, matrix, k):
        n = len(matrix)
        minh = [(matrix[0][i], 0, i) for i in range(n)]
        heapq.heapify(minh)

        for i in range(k-1):
            val, r, c = heapq.heappop(minh)
            if r == n - 1: continue
            heapq.heappush(minh, (matrix[r+1][c], r+1, c))
        
        val, r, c = heapq.heappop(minh)
        return val

    # time limit exceeded
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        res, n = matrix[0], len(matrix)
        for l in range(1, n):
            i, j = 0, 0
            tmp = []
            m = len(res)
            while i < n and j < m:
                if matrix[l][i] < res[j]:
                    tmp.append(matrix[l][i])
                    i += 1
                else:
                    tmp.append(res[j])
                    j += 1
            
            if i < n: tmp += matrix[l][i:]
            if j < m: tmp += res[j:]
            res = tmp
        
        return res[k-1]

    # wrong answer
    def kthSmallest2(self, matrix, k):
        n = len(matrix)
        if n == 1 or k == n*n: return matrix[n-1][n-1]
        a = k // n if k >= n else 1
        b = k - n * (a-1)
        i,j = 0,0
        srt = []
        while i < n and j < n:
            if matrix[a-1][i] < matrix[a][j]:
                srt.append(matrix[a-1][i])
                i += 1
            else:
                srt.append(matrix[a][j])
                j += 1
        if i < n: srt += matrix[a-1][i:]
        if j < n: srt += matrix[a][j:]
        
        return srt[b-1]

sol = Solution()
print(sol.kthSmallest4([[1,5,9],[10,11,13],[12,13,15]], 8))
print(sol.kthSmallest4([[1,2],[1,3]], 4))
