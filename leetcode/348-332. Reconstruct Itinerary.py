# 332. Reconstruct Itinerary
import collections
class Solution:
    def findItinerary(self, tickets):
        d = collections.defaultdict(list)
        for dep, arr in tickets:
            d[dep].append(arr)
        
        for k, v in d.items():
            d[k] = sorted(v)
        
        iti = ["JFK"]
        self.found = False
        def dfs():
            if len(iti) == len(tickets)+1 or self.found:
                self.found = True
                return
            if iti[-1] in d:
                for i in range(len(d[iti[-1]])):
                    iti.append(d[iti[-1]].pop(i))
                    dfs()
                    if self.found: return
                    airp = iti.pop()
                    d[iti[-1]].insert(i, airp)

        dfs()
        return iti

print(Solution().findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))