# 528. Random Pick with Weight
class Solution:

    def __init__(self, w: List[int]):
        self.cum_w = [w[0]]
        for x in w[1:]:
            self.cum_w.append(x + self.cum_w[-1])

    def pickIndex(self) -> int:
        ran = random.randint(1, self.cum_w[-1])
        
        l, r = 0, len(self.cum_w)-1
        while l < r:
            m = (l + r) // 2
            if ran <= self.cum_w[m]:
                r = m
            else:
                l = m + 1
                
        return l
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()