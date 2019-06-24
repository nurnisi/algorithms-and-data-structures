# 539. Minimum Time Difference
class Solution:
    def findMinDifference2(self, timePoints) -> int:
        timePoints.sort()
        ans = float('inf')
        for i in range(len(timePoints)-1):
            h = int(timePoints[i+1][:2]) - int(timePoints[i][:2])
            m = int(timePoints[i+1][3:]) - int(timePoints[i][3:])
            if m < 0: 
                m += 60
                h -= 1
            hm = h * 60 + m
            ans = min(ans, hm)
            
        h1 = int(timePoints[0][:2])
        m1 = int(timePoints[0][3:])
        
        h2 = 24 - int(timePoints[-1][:2])
        m2 = 60 - int(timePoints[-1][3:])
        if m2: h2 -= 1
        
        hm = h1 * 60 + m1 + h2 * 60 + m2
        ans = min(ans, hm)
        
        return ans

    def findMinDifference(self, timePoints) -> int:
        tp = sorted(int(t[:2])*60 + int(t[3:]) for t in timePoints)
        tp.append(1440 + tp[0])
        return min(b - a for a, b in zip(tp, tp[1:]))

print(Solution().findMinDifference(["01:01","02:01","03:00"]))
print(Solution().findMinDifference(["01:01","02:01","03:00","03:01"]))
print(Solution().findMinDifference(["09:00","00:00", "03:00"]))
print(Solution().findMinDifference(["00:23","23:34"]))
