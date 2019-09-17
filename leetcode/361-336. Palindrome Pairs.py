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
    def palindromePairs(self, words):
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
                        
                if j != n and self.isPalindrome(suff):
                    back = pref[::-1]
                    if back in d and d[back] != i:
                        ans.append([i, d[back]])
                        
        return ans

    def isPalindrome(self, w):
        return w == w[::-1]

print(Solution().palindromePairs(["abcd","dcba","lls","s","sssll"]))

#     def palindromePairs(self, words: List[str]) -> List[List[int]]:
#         trie = self.makeTrie(words)
#         print(trie)
#         ans = []
#         for j, w in enumerate(words):
#             i = self.hasPalindrome(trie, w)
#             if i != -1 and i != j:
#                 ans.append([i, j])
#             if 'end' in trie and trie['end'] != j and self.isPalindrome(w):
#                 ans.extend([[trie['end'], j], [j, trie['end']]])
            
#         return ans
        
#     def isPalindrome(self, word):
#         i, j = 0, len(word)-1
#         while i < j:
#             if word[i] != word[j]:
#                 return False
#             i, j = i+1, j-1
#         return True
        
#     def hasPalindrome(self, trie, word):
#         cur = trie
#         i = 1
#         while i <= len(word):
#             if word[-i] not in cur: break
#             cur = cur[word[-i]]   
#             i += 1
            
#         if i <= len(word) and 'end' in cur and len(set(word[:-i+1])) == 1:
#             return cur['end'] 
#         if i > len(word) and 'end' in cur:
#             return cur['end']
#         return -1
        
#     def makeTrie(self, words):
#         root = {}
#         for i, w in enumerate(words):
#             cur = root
#             for ch in w:
#                 cur = cur.setdefault(ch, {})
#             cur['end'] = i
#         return root