# 890. Find and Replace Pattern
class Solution:
    def findAndReplacePattern(self, words, pattern: str):
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
            
print(Solution().findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb"))
                        