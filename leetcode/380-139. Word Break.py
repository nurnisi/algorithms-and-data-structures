# 139. Word Break
class Solution:
    def wordBreak2(self, s: str, wordDict) -> bool:
        if not s or not wordDict:
            return False
        max_len = max(len(w) for w in wordDict)
        wordSet = set(wordDict)
        
        queue = set()
        for i in range(1, max_len+1):
            if s[:i] in wordSet:
                if s[i:] == "":
                    return True
                queue.add(s[i:])
        
        while queue:
            cur = queue.pop()
            for i in range(1, min(max_len, len(cur))+1):
                if cur[:i] in wordSet:
                    if cur[i:] == "":
                        return True
                    queue.add(cur[i:])
                    
        return False

    def wordBreak(self, s: str, wordDict) -> bool:
        n = len(s)
        dp = [True] + [False] * n
        
        for i in range(n):
            for w in wordDict:
                dp[i+1] = dp[i+1] or (w == s[i-len(w)+1:i+1] and dp[i-len(w)+1])
        
        return dp[-1]