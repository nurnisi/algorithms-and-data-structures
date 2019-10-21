# 593. Valid Square
class Solution:
    def validSquare(self, p1, p2, p3, p4):
        def distance(p1, p2):
            return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
        
        points = [p1, p2, p3, p4]
    
        distances = []
        for i in range(4):
            for j in range(i+1, 4):
                if points[i] == points[j]:
                    return False
                distances.append(distance(points[i], points[j]))
  
        return len(set(distances)) == 2