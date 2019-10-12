import collections
def social_network(matrix):
    visited = set()
    ans = 0

    for i in range(len(matrix)):
        q = collections.deque()

        if i not in visited:
            q.append(i)
            visited.add(i)
            ans += 1

        while q:
            cur = q.popleft()
            for j, x in enumerate(matrix[cur]):
                if x and j not in visited:
                    q.append(j)
                    visited.add(j)

    return ans

matrix = [
    [1,1,0,0],
    [1,1,1,0],
    [0,1,1,0],
    [0,0,0,1]
]

matrix = [
    [1,1,0],
    [1,1,0],
    [0,0,1]
]
print(social_network(matrix))


                
