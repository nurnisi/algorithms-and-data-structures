# 207. Course Schedule
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = collections.defaultdict(list)
        for course, prereq in prerequisites:
            d[course].append(prereq)
            
        status = [0] * numCourses
        def canTake(i):
            if status[i] in {1, -1}: return status[i] == 1
            status[i] = -1
            if any(not canTake(j) for j in d[i]): return False
            status[i] = 1
            return True
        
        return all(canTake(i) for i in range(numCourses))
            