def maxDistToClosest(self, seats):
    left, right, l = 0, 0, len(seats)
    while (seats[left] != 1):
        left += 1
    while (seats[l - 1 - right] != 1):
        right += 1

    res, arr, count = max(left, right), [0] * l, 0
    for i in range(l):
        if seats[i] == 1:
            res = max(res, count/2)
            count = 0
        arr[i] = count
        count += 1
    return int(res)
    """
    :type seats: List[int]
    :rtype: int
    """


def maxDistToClosest2(self, seats):
    N = len(seats)
    left, right = [N] * N, [N] * N
    
    for i in range(N):
        if seats[i] == 1: left[i] = 0
        elif i > 0: left[i] = left[i - 1] + 1

    for i in range(N-1, -1, -1):
        if seats[i] == 1: right[i] = 0
        elif i < N - 1: right[i] = right[i + 1] + 1
    
    ans = 0
    for i in range(N): 
        if seats[i] == 0: ans = max(ans, min(left[i], right[i]))
    return ans


def maxDistToClosest2_2(self, seats):
    N = len(seats)
    left, right = [N] * N, [N] * N
    
    for i in range(N):
        if seats[i] == 1: left[i] = 0
        elif i > 0: left[i] = left[i - 1] + 1

    for i in range(N-1, -1, -1):
        if seats[i] == 1: right[i] = 0
        elif i < N - 1: right[i] = right[i + 1] + 1
    
    return max(min(left[i], right[i])
            for i, seat in enumerate(seats) if not seat)


def maxDistToClosest3(self, seats):
    N = len(seats)
    prev, future = -1, 0
    ans = 0

    for i in range(N):
        if seats[i] == 1: prev = i
        else:
            while future < N and seats[future] == 0 or future < i: future+=1
            left = N if prev == -1 else i - prev
            right = N if future == N else future - i
            ans = max(ans, min(left,right))

    return ans


def maxDistToClosest4(self, seats):
    people = (i for i, seat in enumerate(seats) if seat)
    prev, future = None, next(people)
    
    ans = 0
    for i, seat in enumerate(seats):
        if seat:
            prev = i
        else:
            while future is not None and future < i:
                future = next(people, None)
            
            left = float('inf') if prev is None else i - prev
            right = float('inf') if future is None else future - i
            ans = max(ans, min(left, right))
            
    return ans


from itertools import groupby
def maxDistToClosest5(self, seats):
    ans = 0
    for seat, group in groupby(seats):
        if not seat:
            K = len(list(group))
            ans = max(ans, (K + 1)/2)

    return int(max(ans, seats.index(1), seats[::-1].index(1)))