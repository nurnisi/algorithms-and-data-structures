# 973. K Closest Points to Origin
import random
class Solution:
    # Accepted
    def kClosest2(self, points, K):
        dist = []
        for p in points:
            dist.append((p[0]**2 + p[1]**2, p))
        dist.sort()
        ans = []
        for d in dist[:K]:
            ans.append(d[1])
        return ans

    # revisited: sorting
    def kClosest3(self, points, K):
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]

    # quickSelect
    def kClosest(self, points, K):
        rand = random.randint(0, len(points)-1)
        x = points[rand][0]**2 + points[rand][1]**2
        left, right = [], []
        for p in points:
            if p[0]**2 + p[1]**2 > x: right.append(p)
            else: left.append(p)
        if len(left) == K: return left
        elif len(left) < K: return left + self.kClosest(right, K - len(left))
        else: return self.kClosest(left, K)
    


        
sol = Solution()
print(sol.kClosest(points = [[1,3],[-2,2]], K = 1))
print(sol.kClosest(points = [[3,3],[5,-1],[-2,4]], K = 2))
print(sol.kClosest([[-2,10],[-4,-8],[10,7],[-4,-7]], 3))

print(sol.kClosest3(points = [[1,3],[-2,2]], K = 1))
print(sol.kClosest3(points = [[3,3],[5,-1],[-2,4]], K = 2))