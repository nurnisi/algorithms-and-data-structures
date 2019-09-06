# 1176. Diet Plan Performance
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        T = sum(calories[:k])
        ans = 0
        for i in range(k, len(calories)+1):
            if T > upper: ans += 1
            elif T < lower: ans -= 1
            
            if i != len(calories):
                T = T + calories[i] - calories[i-k]
        
        return ans