# 797. All Paths From Source to Target
from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph):        
        ans = []
        self.helper(graph, [], ans, 0)
        return ans
    
    def helper(self, graph, path, ans, i):
        path.append(i)
        if i == len(graph) - 1:
            ans.append(path.copy)

        for j in graph[i]:
            self.helper(graph, path, ans, j)
        
        path.pop()
        
print(Solution().allPathsSourceTarget([[1,2],[3],[3],[]]))