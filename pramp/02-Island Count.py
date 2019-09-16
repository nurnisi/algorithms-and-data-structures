import collections
def get_number_of_islands(binaryMatrix):
  n, m  = len(binaryMatrix), len(binaryMatrix[0])
  visited = set()
  
  dirs = ((0,1), (1,0), (-1,0), (0,-1))
  islands = 0
  
  for i in range(n):
    for j in range(m):
      if binaryMatrix[i][j] == 1 and (i,j) not in visited:
        q = collections.deque([(i, j)])
        visited.add((i, j))
        
        while q:
          ci, cj = q.popleft()
          
          for di, dj in dirs:
            di, dj = di+ci, dj+cj
            if 0 <= di < n and 0 <= dj < m and \
              (di, dj) not in visited and binaryMatrix[di][dj] == 1:
              q.append((di, dj))
              visited.add((di, dj))
        
        islands += 1
        
  return islands