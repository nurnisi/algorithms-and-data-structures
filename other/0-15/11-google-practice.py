def min_days_bloom2(roses, k, n):
    r_sorted = sorted([(x, i) for i, x in enumerate(roses)], reverse=True)
    d = {}
    while r_sorted:
        x, i = r_sorted.pop()
        if i-1 in d and i+1 in d:
            start = d.pop(i-1)
            end = d.pop(i+1)
            d[start] = end
            d[end] = start
        elif i-1 in d:
            start = d.pop(i-1)
            d[start] = i
            d[i] = start
        elif i+1 in d:
            end = d.pop(i+1)
            d[end] = i
            d[i] = end
        else:
            d[i] = i
        
        cnt = 0
        for s, e in d.items():
            cnt += (abs(e - s) + 1) // k
        if cnt // 2 == n:
            return x
    return -1

def min_days_bloom(roses, k, n):
    def suff_bouquets(d):
        m, i, bouq = len(roses), 0, 0
        while i < m:
            if roses[i] > d:
                i += 1
                continue
            j = i
            while j+1 < m and roses[j+1] <= d:
                j += 1
            bouq += (j-i+1)//k
            if bouq >= n:
                return True
            i = j + 1
        return False

    l, r = 0, max(roses)
    while l < r:
        m = (l + r) // 2
        if suff_bouquets(m):
            r = m
        else:
            l = m + 1

    return l

roses = [1, 2, 4, 9, 3, 4, 1]
k = 2
n = 2
print(min_days_bloom(roses, k, n))
