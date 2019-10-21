# 139. Word Break
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        if not s or not wordDict:
            return False
        max_len = max(len(w) for w in wordDict)
        wordSet = set(wordDict)
        
        queue = collections.deque()
        for i in range(1, max_len+1):
            if s[:i] in wordSet:
                if s[i:] == "":
                    return True
                queue.append(s[i:])
        
        while queue:
            cur = queue.popleft()
            for i in range(1, min(max_len, len(cur))+1):
                if cur[:i] in wordSet:
                    if cur[i:] == "":
                        return True
                    queue.append(cur[i:])
                    
        return False