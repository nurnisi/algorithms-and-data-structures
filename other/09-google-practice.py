import heapq
def min_chairs(S, E):
    heap, ans = [], 0
    
    for s, e in sorted(zip(S, E)):
        while heap and heap[0] <= s:
            heapq.heappop(heap)
        heapq.heappush(heap, e)
        ans = max(ans, len(heap))
    
    return ans

S = [1, 2, 6, 5, 3]
E = [5, 5, 7, 6, 8]    

print(min_chairs(S, E))

