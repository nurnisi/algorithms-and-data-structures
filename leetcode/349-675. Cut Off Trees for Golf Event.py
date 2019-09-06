# 675. Cut Off Trees for Golf Event
import collections, heapq
class Solution:
    def cutOffTree(self, forest) -> int:
        heap = []
        m, n = len(forest), len(forest[0])
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    heapq.heappush(heap, (forest[i][j], i, j))
        
        def getMinSteps(si, sj, ei, ej):
            minPath = [[0 if tree == 0 else -1 for tree in row] for row in forest]
            dirs = ((0,1), (1,0), (0,-1), (-1,0))
            
            queue = collections.deque([(si, sj)])
            minPath[si][sj] = steps = 0

            while queue:
                size = len(queue)
                steps += 1
                for _ in range(size):
                    ci, cj = queue.popleft()
                    if ci == ei and cj == ej:
                        return minPath[ci][cj]

                    for di, dj in dirs:
                        di, dj = di+ci, dj+cj
                        if 0 <= di < m and 0 <= dj < n and minPath[di][dj] == -1:
                            queue.append((di, dj))
                            minPath[di][dj] = steps
                
            return -1
        
        minSteps = 0
        curi, curj = 0, 0
        while heap:
            height, nexti, nextj = heapq.heappop(heap)
            steps = getMinSteps(curi, curj, nexti, nextj)
            if steps == -1:
                return -1
            minSteps += steps
            curi, curj = nexti, nextj
        
        return minSteps

print(Solution().cutOffTree([[54581641,64080174,24346381,69107959],[86374198,61363882,68783324,79706116],[668150,92178815,89819108,94701471],[83920491,22724204,46281641,47531096],[89078499,18904913,25462145,60813308]]))