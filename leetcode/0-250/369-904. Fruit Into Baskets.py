# 904. Fruit Into Baskets
import collections
class Solution:
    def totalFruit(self, tree) -> int:
        d = collections.OrderedDict()
        n, prev, ans = len(tree), -1, 0
        for i, t in enumerate(tree):
            d.pop(t, 0)
            d[t] = i
            if len(d) > 2:
                ans = max(ans, i - prev - 1)
                t, prev = d.popitem(last=False)
        return max(ans, i - prev)

print(Solution().totalFruit([1,2,1]))
print(Solution().totalFruit([0,1,2,2]))
print(Solution().totalFruit([1,2,3,2,2]))
print(Solution().totalFruit([3,3,3,1,2,1,1,2,3,3,4]))