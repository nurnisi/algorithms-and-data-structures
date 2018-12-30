# 967. Numbers With Same Consecutive Differences
import collections
class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return [i for i in range(10)]

        d = collections.defaultdict(list)
        for i in range(10):
            for j in range(10):
                if abs(i-j) == K:
                    d[str(i)].append(str(j))

        d = dict(d)
        ans = []
        # print(d)

        def helper(cur, i, arr):
            if i == N:
                ans.append(int(''.join(arr)))
            else:
                nextNums = d[cur]
                for num in nextNums:
                    helper(num, i+1, arr+[num])
        
        for k in d.keys():
            if k != '0':
                helper(k, 1, [k])

        return ans

sol = Solution()
# print(sol.numsSameConsecDiff(3, 7))
# print(sol.numsSameConsecDiff(2, 1))
print(sol.numsSameConsecDiff(1, 0))