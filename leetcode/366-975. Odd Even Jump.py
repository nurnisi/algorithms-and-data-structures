# 975. Odd Even Jump
import heapq
class Solution:
    # brute force: TLE
    def oddEvenJumps2(self, A):
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

    # min and max heaps: TLE
    def oddEvenJumps3(self, A):
        n = len(A)
        jumps = [[False, False] for _ in A]
        jumps[n-1] = [True, True]
        minheap, maxheap = [(A[n-1], n-1)], []
        
        cnt = 1
        for i in range(n-2, -1, -1):
            while minheap and A[i] > minheap[0][0]:
                v, idx = heapq.heappop(minheap)
                heapq.heappush(maxheap, (-v, idx))
            
            while maxheap and A[i] <= -maxheap[0][0]:
                v, idx = heapq.heappop(maxheap)
                heapq.heappush(minheap, (-v, idx))
            
            if minheap:
                jumps[i][0] = jumps[minheap[0][1]][1]

            if minheap and minheap[0][0] == A[i]:
                jumps[i][1] = jumps[minheap[0][1]][0]
            elif maxheap:
                jumps[i][1] = jumps[maxheap[0][1]][0]
            
            heapq.heappush(minheap, (A[i], i))
            
            cnt += 1 if jumps[i][0] else 0
        
        return cnt

    # binary search: TLE
    def oddEvenJumps(self, A):
        n = len(A)
        jumps = [[False, False] for _ in A]
        jumps[n-1] = [True, True]
        a_sorted = [[A[n-1], n-1]]
        
        cnt = 1
        for i in range(n-2, -1, -1):
            l, r = 0, len(a_sorted)
            while l < r:
                m = (l+r)//2
                if a_sorted[m][0] < A[i]:
                    l = m+1
                else:
                    r = m
            
            left, right = a_sorted[:l], a_sorted[l:]
            if right and right[0][0] == A[i]:
                jumps[i][0] = jumps[right[0][1]][1]
                jumps[i][1] = jumps[right[0][1]][0]
                a_sorted[l][1] = i
            else:
                if left:
                    jumps[i][1] = jumps[left[-1][1]][0]
                if right:
                    jumps[i][0] = jumps[right[0][1]][1]
                a_sorted.insert(l, [A[i], i])
            
            cnt += 1 if jumps[i][0] else 0
            
        return cnt

A = [10,13,12,14,15]
A = [2,3,1,1,4]
A = [5,1,3,4,2]
A = [1,2,3,2,1,4,4,5]
print(Solution().oddEvenJumps(A))