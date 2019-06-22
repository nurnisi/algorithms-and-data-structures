# 890. Find and Replace Pattern
class Solution:
    def findAndReplacePattern2(self, words, pattern: str):
        ans = []
        for w in words:
            d = {}
            flag = True
            if len(w) == len(pattern):
                for i in range(len(w)):
                    if w[i] in d and d[w[i]] != pattern[i] \
                        or pattern[i] in d and d[pattern[i]] != w[i]:
                        flag = False
                        break
                    else:
                        d[w[i]] = pattern[i]
                        d[pattern[i]] = w[i]
                if flag:
                    ans.append(w)   
        
        return ans

    def findAndReplacePattern(self, words, pattern: str):
        def match(word):
            dw, dp = {}, {}
            for w, p in zip(word, pattern):
                if w not in dw: dw[w] = p
                if p not in dp: dp[p] = w
                if (dw[w], dp[p]) != (p, w): return False
            return True
        
        return list(filter(match, words))

            
print(Solution().findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb"))
                        