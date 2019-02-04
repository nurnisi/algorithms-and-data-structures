def solution2(S, E):
    arr = [0] * 1001
    for i in range(len(S)):
        for j in range(S[i], E[i]):
            arr[j] += 1
    
    return max(arr)


import heapq
def solution(S, E):
    quests = [(S[i], E[i]) for i in range(len(S))]
    quests.sort(key=lambda q: q[0])

    ans = 0
    heap = []
    for come, leave in quests:
        cur = ans
        while heap and heap[0] <= come:
            heapq.heappop(heap)
            cur -= 1
        heapq.heappush(heap, leave)
        cur += 1
        ans = max(ans, cur)
    
    return ans
    
print(solution([1,2,6,5,3], [5,5,7,6,8]))
print(solution([1,2,6,5,3,4],[6,6,7,6,8,6]))
print(solution2([1,2,6,5,3], [5,5,7,6,8]))
print(solution2([1,2,6,5,3,4],[6,6,7,6,8,6]))