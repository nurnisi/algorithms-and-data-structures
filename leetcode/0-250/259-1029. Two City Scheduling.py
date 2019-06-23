# 1029. Two City Scheduling
class Solution:
    def twoCitySchedCost(self, costs) -> int:
        costs = sorted(costs, key=lambda x: x[0] - x[1])
        return sum([x[0] for x in costs[:len(costs)//2]]) \
                + sum([x[1] for x in costs[len(costs)//2:]])

print(Solution().twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))