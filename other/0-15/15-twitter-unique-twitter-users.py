def unique_twitter_ids2(arr):
    a_srt = sorted(arr) + [float('inf')]
    i = dups = sm = 0
    n = len(a_srt)
    while i < n-1:
        if a_srt[i] == a_srt[i+1]:
            dups += 1
        else:
            sm += a_srt[i]
            cur = a_srt[i] + 1
            while cur < a_srt[i+1] and dups > 0:
                sm += cur
                cur += 1
                dups -= 1
        i += 1
    
    return sm

def unique_twitter_ids(arr):
    sm = low = 0
    for x in sorted(arr):
        low = max(low+1, x)
        sm += low
    return sm

print(unique_twitter_ids([3,2,1,2,7]))