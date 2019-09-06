def triplets(t, d):
    ans = 0
    l, r = 0, len(d)-1
    d.sort()
    while l < r and d[l]+d[l+1]+d[r] <= t:
        ll, rr, mid = l, r, l
        while ll < rr:
            mid = (ll + rr) // 2
            if d[l]+d[mid]+d[r] == t:
                break
            elif d[l]+d[mid]+d[r] < t:
                ll = mid + 1
            else:
                rr = mid
        ans += mid - l
        l += 1
        r -= 1
    return ans

def triplets2(t, d):
    d.sort()
    ans, n = 0, len(d)
    for i in range(n-2):
        l = i+1
        r = n-1
        while l < r:
            if d[i]+d[l]+d[r] == t:
                break
            if d[i]+d[l]+d[r] < t:
                l += 1
            else:
                r -= 1
        ans += (l-i) * (r-l)
    
    return ans

import heapq
def maxEvents(arrival, duration):
    heap = []
    depart = [arrival[i] + duration[i] for i in range(len(arrival))]
    
    for a, d in sorted(zip(arrival, depart)):
        if not heap or -heap[0] <= a:
            heapq.heappush(heap, -d)
    
    return len(heap)
    

print(maxEvents([1,3,3,5,7], [2,2,1,2,1]))
# print(triplets2(8, [1,2,3,4,5]))