import collections, math
def max_cake_area(radii, guests):
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

# radii = [1, 1, 1, 2, 2, 3]
# numberOfGuests = 6

# radii = [4, 3, 3]
# numberOfGuests = 3

radii = [6, 7]
numberOfGuests = 12

print(max_cake_area(radii, numberOfGuests))