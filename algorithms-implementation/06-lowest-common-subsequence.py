# Lowest Common Subsequence
"""
Example:
input: "abcdef" and "acdcf"
output: "acdf"
"""
class lcs:
    def count_lcs(self, str1, str2):
        # create a dp array
        n1, n2 = len(str1)+1, len(str2)+1
        dp = [[0] * n2 for _ in range(n1)]

        for i in range(1, n1):
            for j in range(1, n2):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1 # if there is a match increment
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # max otherwise

        ans = []
        self.get_all_lcs(str1, str2, dp, i, j, "", ans)
        for s in ans: print(s)

        return dp[-1][-1]

    # get a single lcs
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

    # get all lcs
    def get_all_lcs(self, str1, str2, dp, i, j, cur, ans):
        if i == 0 or j == 0:
            ans.append(cur)
            return
        
        if str1[i-1] == str2[j-1]: # if chars are equal, appendleft the char
            self.get_all_lcs(str1, str2, dp, i-1, j-1, str1[i-1] + cur, ans)
        
        else:
            if dp[i-1][j] >= dp[i][j-1]: # go top
                self.get_all_lcs(str1, str2, dp, i-1, j, cur, ans)
            if dp[i][j-1] >= dp[i-1][j]: # go left
                self.get_all_lcs(str1, str2, dp, i, j-1, cur, ans)
        

print(lcs().count_lcs("ABCBDAB", "BDCABA"))