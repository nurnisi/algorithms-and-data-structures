import collections, math
def max_cake_area2(radii, guests):
    cnts = collections.Counter([x*x for x in radii])
    cnts_sorted = sorted(cnts.items(), key=lambda kv: kv[1], reverse=True)

    if len(cnts_sorted) == 1:
        return math.pi * cnts[0] / guests
    
    ar1, gst1 = cnts_sorted[-2]
    ar2, gst2 = cnts_sorted[-1]
    i = guests
    while ar2 * gst2 / (i-1) < ar1 * gst1 / (guests-i+1):
        i -= 1
    
    if gst1 + gst2 >= guests:
        return ar1 * math.pi
    return ar2 * math.pi * gst2 / i

def max_cake_area(radii, guests):
    areas = [math.pi*r*r for r in radii]

    def possible(x):
        k = 0
        for a in areas:
            k += a // x
            if k >= guests:
                return True
        return False

    l, r = 0, max(areas)
    while l + 1e-5 <= r:
        x = (l + r) / 2
        if possible(x):
            l = x
        else:
            r = x

    return round(x, 4)

def getMaxCake(cakes, P):
    def getArea(cake):
        return math.pi * cake * cake
    
    N = len(cakes)
    dp = []
    for i in range(P + 1):
        dp.append([0] * (N + 1))

    for i in range(1, N + 1):
        dp[1][i] = getArea(cakes[i - 1])

    for p in range(2, P + 1):
        for i in range(1, N + 1):
            iarea = getArea(cakes[i - 1])
            dp[p][i] = iarea / p
            for j in range(1, P + 1):
                dp[p][i] = max(min(dp[p - j][i - 1], iarea / j), 
                                dp[p][i])

    return round(dp[P][N], 4)

radii = [1, 1, 1, 2, 2, 3]
numberOfGuests = 6
print(getMaxCake(radii, numberOfGuests))

radii = [4, 3, 3]
numberOfGuests = 3
print(getMaxCake(radii, numberOfGuests))

radii = [6, 7]
numberOfGuests = 12
print(getMaxCake(radii, numberOfGuests))