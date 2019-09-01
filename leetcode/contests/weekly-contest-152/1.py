class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        sm = sum(calories[:k])
        pts = 0
        if sm > upper: pts += 1
        elif sm < lower: pts -= 1
            
        for i in range(k, len(calories)):
            sm = sm + calories[i] - calories[i-k]
            if sm > upper: pts += 1
            elif sm < lower: pts -= 1
            
        return pts