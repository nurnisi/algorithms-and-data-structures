def solution(S, E):
    n = len(S)
    arr = [(S[i], E[i]) for i in range(n)]
    arr.sort()
    print(arr)
    seats = 1
    prev = 0
    for i in range(1, n):
        if arr[i-1][1] > arr[i][1]:
            seats = max(seats, i - prev)
            prev = i

    return seats

def solution2(S, E):
    n = len(S)
    arr = [(E[i], S[i]) for i in range(n)]
    arr.sort()
    print(arr)
    seats = 1
    prev = 0
    for i in range(1, n):
        if arr[i-1][1] > arr[i][1]:
            seats = max(seats, i - prev)
            prev = i

    return seats

print(solution([1,2,6,5,3,4],[6,6,7,6,8,6]))
print(solution2([1,2,6,5,3,4],[6,6,7,6,8,6]))