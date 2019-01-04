def solution(S, E):
    arr = [0] * 1001
    for i in range(len(S)):
        for j in range(S[i], E[i]):
            arr[j] += 1
    
    return max(arr)
    
print(solution([1,2,6,5,3], [5,5,7,6,8]))
print(solution([1,2,6,5,3,4],[6,6,7,6,8,6]))