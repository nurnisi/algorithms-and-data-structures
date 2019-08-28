# 1086. High Five
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        d = collections.defaultdict(list)
        for sid, score in items:
            heapq.heappush(d[sid], score)
            if len(d[sid]) > 5: heapq.heappop(d[sid])
        
        return [[sid, sum(val)//5] for sid, val in d.items()]
        