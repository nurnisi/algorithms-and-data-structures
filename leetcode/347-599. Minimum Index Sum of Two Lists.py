# 599. Minimum Index Sum of Two Lists
import heapq
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {res: idx for idx, res in enumerate(list1)}
        heap = []
        
        for idx, res in enumerate(list2):
            if res in d:
                heapq.heappush(heap, (idx + d[res], res))
        
        lis = heap[0][0]
        ans = []
        while heap and heap[0][0] == lis:
            ans.append(heapq.heappop(heap)[1])
        
        return ans