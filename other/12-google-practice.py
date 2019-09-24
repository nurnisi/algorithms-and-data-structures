def decreasing_subsequences(A):
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

A = [5, 2, 4, 3, 1, 6]
A = [2, 9, 12, 13, 4, 7, 6, 5, 10]
A = [1, 1, 1]
print(decreasing_subsequences(A))
        


