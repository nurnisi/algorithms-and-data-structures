import heapq

def fountainActivation(ftns):
    ftRange = []
    n = len(ftns)
    for i, f in enumerate(ftns):
        heapq.heappush(ftRange, [max(i-f+1, 1), min(i+f+1, n)])
    
    print(ftRange)

    ans = 1
    prev = heapq.heappop(ftRange)
    while ftRange:
        cur = heapq.heappop(ftRange)
        if prev[0] == cur[0]:
            prev[1] = max(prev[1], cur[1])
        elif prev[1] < cur[1]:
            ans += 1
            prev = cur
            
    return ans

print(fountainActivation([1,2,1]))
print(fountainActivation([1,1,1,1]))
print(fountainActivation([1,0,1]))
print(fountainActivation([0,0,0]))
