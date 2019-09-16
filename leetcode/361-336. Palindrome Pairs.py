# 336. Palindrome Pairs
# bruteforce: TLE
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans = []
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if self.isPalindrome(words[i]+words[j]):
                    ans.append([i,j])
                if self.isPalindrome(words[j]+words[i]):
                    ans.append([j,i])
                    
        return ans
        
    def isPalindrome(self, w):
        i, j = 0, len(w)-1
        while i < j:
            if w[i] != w[j]:
                return False
            i, j = i+1, j-1
            
        return True