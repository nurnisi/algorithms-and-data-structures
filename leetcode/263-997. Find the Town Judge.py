# 997. Find the Town Judge
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        people = [[0, 0] for _ in range(N)]
        for a, b in trust:
            people[a - 1][0] += 1
            people[b - 1][1] += 1
        
        for i in range(N):
            if not people[i][0] and people[i][1] == N - 1:
                return i + 1
        
        return -1