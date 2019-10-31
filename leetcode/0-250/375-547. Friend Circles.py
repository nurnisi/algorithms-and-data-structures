# 547. Friend Circles
import collections
class Solution:
    # bfs
    def findCircleNum2(self, M: List[List[int]]) -> int:
        visited = set()
        ans = 0

        for i in range(len(M)):
            q = collections.deque()

            if i not in visited:
                q.append(i)
                visited.add(i)
                ans += 1

            while q:
                cur = q.popleft()
                for j, x in enumerate(M[cur]):
                    if x and j not in visited:
                        q.append(j)
                        visited.add(j)

        return ans

    # union find
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if M[i][j]:
                    uf.union(i, j)

        return len(uf.items)
    
class UnionFind:
    def __init__(self, n):
        self.items = [set([i]) for i in range(n)]

    def find_index(self, item):
        for i, x in enumerate(self.items):
            if item in x:
                return i

    def union(self, a, b):
        ai = self.find_index(a)
        bi = self.find_index(b)

        if ai != bi:
            self.items[ai] |= self.items[bi]
            self.items.pop(bi)