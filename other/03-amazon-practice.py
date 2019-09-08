import collections
def treasureIsland(matrix):
    q = collections.deque([(0,0,0)])
    matrix[0][0] = 'V'
    n = len(matrix)
    dirs = ((0,1),(1,0),(0,-1),(-1,0))

    while q:
        i, j, st = q.popleft()
        for di, dj in dirs:
            di, dj = di+i, dj+j
            if 0 <= di < n and 0 <= dj < n:
                if matrix[di][dj] == 'X':
                    return st+1
                elif matrix[di][dj] == 'O':
                    q.append((di, dj, st+1))
                    matrix[di][dj] = 'V'

    return -1

def treasureIsland2(matrix):
    min_dist = float('inf')
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'S':
                matrix_copy = [row[:] for row in matrix]
                min_dist = min(min_dist, bfs(matrix_copy, i, j))

    return min_dist

def bfs(matrix, si, sj):
    q = collections.deque([(si,sj,0)])
    matrix[si][sj] = 'V'
    n = len(matrix)
    dirs = ((0,1),(1,0),(0,-1),(-1,0))

    while q:
        i, j, st = q.popleft()
        for di, dj in dirs:
            di, dj = di+i, dj+j
            if 0 <= di < n and 0 <= dj < n:
                if matrix[di][dj] == 'X':
                    return st+1
                elif matrix[di][dj] == 'O':
                    q.append((di, dj, st+1))
                    matrix[di][dj] = 'V'

    return float('inf')

            
print(treasureIsland([['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]))

print(treasureIsland2([['S', 'O', 'O', 'S', 'S'],
 ['D', 'O', 'D', 'O', 'D'],
 ['O', 'O', 'O', 'O', 'X'],
 ['X', 'D', 'D', 'O', 'O'],
 ['X', 'D', 'D', 'D', 'O']]))

