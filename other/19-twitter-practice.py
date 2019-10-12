import heapq

# nlogn
def fountainActivation2(ftns):
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

# n
def fountainActivation(ftns):
    n = len(ftns)
    right_most = [0] * n
    for i, x in enumerate(ftns):
        l, r = max(i-x, 0), min(i+x+1, n)
        right_most[l] = max(right_most[l], r)

    ans = 1
    r, next_r = right_most[0], 0
    for i in range(n):
        next_r = max(next_r, right_most[i])
        if i == r:
            ans += 1
            r = next_r
    
    return ans

print(fountainActivation([1,2,1]))
print(fountainActivation([1,1,1,1]))
print(fountainActivation([1,0,1]))
print(fountainActivation([0,0,0]))
