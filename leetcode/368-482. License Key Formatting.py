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

    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = ''.join(S.split('-')).upper()[::-1]
        return '-'.join(S[i:i+K] for i in range(0, len(S), K))[::-1]