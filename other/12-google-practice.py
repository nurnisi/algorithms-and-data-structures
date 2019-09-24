# invalid for some cases
def decreasing_subsequences2(A):
    subs = []
    for x in A:
        appended = False
        for i in range(len(subs)):
            if subs[i] > x:
                subs[i] = x
                appended = True
                break
        if not appended:
            subs.append(x)
    
    return len(subs)

# binary search
def decreasing_subsequences(A):
    lasts = []
    def binary(x):
        l, r = 0, len(lasts)
        while l < r:
            m = (l + r) // 2
            if lasts[m] <= x:
                l = m + 1
            else:
                r = m
        return l


    for x in A:
        i = binary(x)
        if i == len(lasts):
            lasts.append(x)
        else:
            lasts[i] = x
    return len(lasts)

A = [5, 2, 4, 3, 1, 6]
A = [2, 9, 12, 13, 4, 7, 6, 5, 10]
A = [1, 1, 1]
print(decreasing_subsequences(A))
        


