# 547. Friend Circles
import collections
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
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