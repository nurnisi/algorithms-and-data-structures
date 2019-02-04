# 973. K Closest Points to Origin
import random
import heapq
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
    def kClosest4(self, points, K):
        rand = random.randint(0, len(points)-1)
        x = points[rand][0]**2 + points[rand][1]**2
        left, right = [], []
        for p in points:
            if p[0]**2 + p[1]**2 > x: right.append(p)
            else: left.append(p)
        if len(left) == K: return left
        elif len(left) < K: return left + self.kClosest(right, K - len(left))
        else: return self.kClosest(left, K)
    
    # quickSelect 2
    def kClosest5(self, points, K):
        arr = [(p[0]**2 + p[1]**2, p) for p in points]
        arr = self.helper(arr, K)
        return [p[1] for p in arr]

    def helper(self, points, K):
        rand = random.randint(0, len(points)-1)
        x = points[rand][0]
        left, right = [], []
        for p in points:
            if p[0] > x: right.append(p)
            else: left.append(p)
        if len(left) == K: return left
        elif len(left) < K: return left + self.helper(right, K - len(left))
        else: return self.helper(left, K)

    # quickSelect 3
    def kClosest6(self, points, K):
        dist = [(p[0]**2 + p[1]**2, p) for p in points]
        self.helper2(dist, 0, len(dist)-1, K)
        return [p[1] for p in dist[:K]]

    def helper2(self, dist, i, j, K):
        oi, oj, r = i, j, dist[random.randint(i, j)]
        while i < j:
            if dist[i][0] >= r[0] and dist[j][0] < r[0]:
                dist[i], dist[j] = dist[j], dist[i]
            if dist[i][0] < r[0]: i += 1
            if dist[j][0] >= r[0]: j -= 1
        if i < K: self.helper2(dist, i, oj, K)
        elif i > K: self.helper2(dist, oi, i, K)
            
    # quickSelect 4: leetcode solution
    def kClosest7(self, points, K):
        dist = lambda i: points[i][0]**2 + points[i][1]**2

        def work(i, j, K):
            if i >= j: return
            oi, oj = i, j
            pivot = dist(random.randint(i, j))
            while i < j:
                while i < j and dist(i) < pivot: i += 1
                while i < j and dist(i) > pivot: j -= 1
                points[i], points[j] = points[j], points[i]
            
            if K <= i - oi + 1: work(oi, i, K)
            else: work(i, oj, K - (i  - oi + 1))
        
        work(0, len(points) - 1, K)
        return points[:K]

    # one liner
    def kClosest(self, points, K):
        return heapq.nsmallest(K, points, lambda p: p[0] * p[0] + p[1] * p[1])
        
sol = Solution()
print(sol.kClosest(points = [[1,3],[-2,2]], K = 1))
print(sol.kClosest(points = [[3,3],[5,-1],[-2,4]], K = 2))
print(sol.kClosest([[-2,10],[-4,-8],[10,7],[-4,-7]], 3))

# print(sol.kClosest2(points = [[1,3],[-2,2]], K = 1))
# print(sol.kClosest2(points = [[3,3],[5,-1],[-2,4]], K = 2))
# print(sol.kClosest2([[-2,10],[-4,-8],[10,7],[-4,-7]], 3))

# print(sol.kClosest3(points = [[1,3],[-2,2]], K = 1))
# print(sol.kClosest3(points = [[3,3],[5,-1],[-2,4]], K = 2))