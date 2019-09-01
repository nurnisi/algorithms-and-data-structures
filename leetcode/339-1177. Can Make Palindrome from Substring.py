# 1177. Can Make Palindrome from Substring
class Solution:
    # Brute force: TLE
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        ans = []
        for q in queries:
            l, r, k = q[0], q[1], q[2]
            cnt = sum([v % 2 for v in collections.Counter(s[l:r+1]).values()])
            ans.append(cnt // 2 <= k)
        return ans

    # DP: TLE
    def canMakePaliQueries(self, s: str, queries):
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

print(Solution().canMakePaliQueries("abcdeaaa", [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]))