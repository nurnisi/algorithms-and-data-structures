# 482. License Key Formatting
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = ''.join(S.split('-')).upper()
        ans, n = [], len(S)
        nk = n % K
        if nk != 0:
            ans.append(S[:nk])
        for i in range(nk, n, K):
            ans.append(S[i:i+K])
        return '-'.join(ans)