# 256. Paint House
import heapq
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        p_red = p_gre = p_blu = 0
        for red, gre, blu in costs:
            c_red = min(p_gre, p_blu) + red
            c_gre = min(p_red, p_blu) + gre
            c_blu = min(p_red, p_gre) + blu
            
            p_red = c_red
            p_gre = c_gre
            p_blu = c_blu
            
        return min(p_red, p_gre, p_blu)     