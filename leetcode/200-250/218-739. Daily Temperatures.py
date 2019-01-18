# 739. Daily Temperatures
import collections
class Solution:
    # TLE
    def dailyTemperatures2(self, T):
        stack, ans = [], [0]*len(T)
        for i in range(len(T)):
            new = []
            while stack:
                t, j = stack.pop()
                if t < T[i]: ans[j] = i - j
                else: new.append((t, j))
            new.append((T[i], i))
            stack = new.copy()
        return ans

    # dictionary
    def dailyTemperatures3(self, T):
        d = collections.defaultdict(list)
        ans = [0]*len(T)
        for i in range(len(T)):
            temp = collections.defaultdict(list)
            for key, val in d.items():
                if key < T[i]:
                    for v in val:
                        ans[v] = i - v
                else: temp[key] = val
            d = temp.copy()
            d[T[i]].append(i)
        return ans

    # stack
    def dailyTemperatures(self, T):
        stack, ans = [], [0]*len(T)
        for i in range(len(T)):
            new, flag = [], True
            while stack:
                t, arrj = stack.pop()
                if t < T[i]:
                    for j in arrj:
                        ans[j] = i - j
                elif t == T[i]:
                    flag = False
                    new.append((t, arrj + [i]))
                else: new.append((t, arrj))
            if flag: new.append((T[i], [i]))
            stack = new.copy()
        return ans

sol = Solution()
print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(sol.dailyTemperatures([73, 73, 73, 73, 73, 73, 73, 73]))