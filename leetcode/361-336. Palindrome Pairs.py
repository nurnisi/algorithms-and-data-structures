# 336. Palindrome Pairs
class Solution:
    # bruteforce: TLE
    def palindromePairs2(self, words):
        ans = []
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if self.isPalindrome(words[i]+words[j]):
                    ans.append([i,j])
                if self.isPalindrome(words[j]+words[i]):
                    ans.append([j,i])
                    
        return ans
        
    def isPalindrome2(self, w):
        i, j = 0, len(w)-1
        while i < j:
            if w[i] != w[j]:
                return False
            i, j = i+1, j-1
            
        return True

    # Prefix / suffix solution
    def palindromePairs3(self, words):
        d = {w:i for i, w in enumerate(words)}
        ans = []
        
        for i, w in enumerate(words):
            n = len(w)
            for j in range(n+1):
                pref = w[:j]
                suff = w[j:]
                if self.isPalindrome(pref):
                    back = suff[::-1]
                    if back in d and d[back] != i:
                        ans.append([d[back], i])
                        
                if j != n and self.isPalindrome3(suff):
                    back = pref[::-1]
                    if back in d and d[back] != i:
                        ans.append([i, d[back]])
                        
        return ans

    def isPalindrome3(self, w):
        return w == w[::-1]
    
    # Trie solution
    def palindromePairs(self, words):
        trie = self.makeTrie(words)
        ans = []
        for j, w in enumerate(words):
            n = len(w)
            for k in range(n+1):
                pref = w[:k]
                suff = w[k:]
                if pref == pref[::-1]:
                    back = suff[::-1]
                    i = self.search(trie, back)        
                    if i != -1 and i != j:
                        ans.append([i, j])                
                
                if k != n and suff == suff[::-1]:
                    back = pref[::-1]
                    i = self.search(trie, back)
                    if i != -1 and i != j:
                        ans.append([j, i])
        return ans
        
    def search(self, trie, word):
        cur = trie
        i = 0
        while i < len(word):
            if word[i] not in cur: return -1
            cur = cur[word[i]]   
            i += 1
        if 'end' in cur:
            return cur['end']
        return -1
        
    def makeTrie(self, words):
        root = {}
        for i, w in enumerate(words):
            cur = root
            for ch in w:
                cur = cur.setdefault(ch, {})
            cur['end'] = i
        return root

print(Solution().palindromePairs(["abcd","dcba","lls","s","sssll"]))