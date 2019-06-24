# Lowest Common Subsequence
class lcs:
    def count_lcs(self, str1, str2):
        n1, n2 = len(str1)+1, len(str2)+1
        dp = [[0] * n2 for _ in range(n1)]

        for i in range(1, n1):
            for j in range(1, n2):
                if str1[i-1] == str2[j-1]: 
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        print(self.get_lcs(str1, str2, dp))

        return dp[-1][-1]

    def get_lcs(self, str1, str2, dp):
        ans = []

        i, j = len(str1), len(str2)
        while i > 0 and j > 0:
            if dp[i][j] - 1 == dp[i-1][j-1]:
                ans.insert(0, str1[i-1])
                i -= 1
                j -= 1
            elif dp[i][j] == dp[i-1][j]:
                i -= 1
            else:
                j -= 1
        
        return ''.join(ans)

print(lcs().count_lcs("abcdef", "acdcf"))