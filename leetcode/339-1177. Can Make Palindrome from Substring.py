# 1177. Can Make Palindrome from Substring
import collections
class Solution:
    # Brute force: TLE
    def canMakePaliQueries2(self, s: str, queries):
        ans = []
        for q in queries:
            l, r, k = q[0], q[1], q[2]
            cnt = sum([v % 2 for v in collections.Counter(s[l:r+1]).values()])
            ans.append(cnt // 2 <= k)
        return ans

    # DP: TLE
    def canMakePaliQueries3(self, s: str, queries):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            cnt = 0
            letters = [0] * 26
            for j in range(i, n):
                ix = ord(s[j]) - ord('a')
                if letters[ix] == 0:
                    cnt += 1
                    letters[ix] = 1
                else:
                    cnt -= 1
                    letters[ix] = 0
                dp[i][j] = cnt//2
        
        ans = []
        for q in queries:
            l, r, k = q[0], q[1], q[2]
            ans.append(dp[l][r] <= k)
        return ans

    def canMakePaliQueries4(self, s: str, queries):
        cnt = [[0] * 26]
        for i, c in enumerate(s):
            cnt.append(cnt[i][:])
            cnt[i+1][ord(c) - ord('a')] += 1
        return [sum((cnt[hi+1][i] - cnt[lo][i]) % 2 for i in range(26)) // 2 <= k for lo, hi, k in queries]

    def canMakePaliQueries(self, s: str, queries):
        odds = [[False] * 26]
        for i, c in enumerate(s):
            odds.append(odds[i][:])
            odds[i+1][ord(c) - ord('a')] ^= True
        return [sum(odds[hi+1][i] ^ odds[lo][i] for i in range(26)) // 2 <= k for lo, hi, k in queries]

print(Solution().canMakePaliQueries("abcdeaaa", [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]))