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
            
print(treasureIsland([['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]))

