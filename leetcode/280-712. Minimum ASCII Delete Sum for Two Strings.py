# 712. Minimum ASCII Delete Sum for Two Strings
class Solution:
    def minimumDeleteSum2(self, s1: str, s2: str) -> int:
        dp = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]

        for i in range(len(s1)-1, -1, -1):
            dp[i][len(s2)] = dp[i+1][len(s2)] + ord(s1[i])

        for i in range(len(s2)-1, -1, -1):
            dp[len(s1)][i] = dp[len(s1)][i+1] + ord(s2[i])

        for i in range(len(s1)-1, -1, -1):
            for j in range(len(s2)-1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j] + ord(s1[i]), dp[i][j+1] + ord(s2[j]))

        return dp[0][0]

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        l1, l2 = len(s1)+1, len(s2)+1
        dp = [[0] * l2 for _ in range(l1)]

        for i in range(1, l1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        for j in range(1, l2):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])

        for i in range(1, l1):
            for j in range(1, l2):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))

        return dp[i][j]    

print(Solution().minimumDeleteSum("sea", "eat"))

print(Solution().minimumDeleteSum("igijekdtywibepwonjbwykkqmrgmtybwhwjiqudxmnniskqjfbkpcxukrablqmwjndlhblxflgehddrvwfacarwkcpmcfqnajqfxyqwiugztocqzuikamtvmbjrypfqvzqiwooewpzcpwhdejmuahqtukistxgfafrymoaodtluaexucnndlnpeszdfsvfofdylcicrrevjggasrgdhwdgjwcchyanodmzmuqeupnpnsmdkcfszznklqjhjqaboikughrnxxggbfyjriuvdsusvmhiaszicfa", "ikhuivqorirphlzqgcruwirpewbjgrjtugwpnkbrdfufjsmgzzjespzdcdjcoioaqybciofdzbdieegetnogoibbwfielwungehetanktjqjrddkrnsxvdmehaeyrpzxrxkhlepdgpwhgpnaatkzbxbnopecfkxoekcdntjyrmmvppcxcgquhomcsltiqzqzmkloomvfayxhawlyqxnsbyskjtzxiyrsaobbnjpgzmetpqvscyycutdkpjpzfokvi"))