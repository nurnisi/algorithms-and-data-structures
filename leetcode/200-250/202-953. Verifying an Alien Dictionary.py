# 953. Verifying an Alien Dictionary
class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        d = {}
        for i, v in enumerate(order):
            d[v] = i
        
        for i in range(len(words)-1):
            j = 0
            while j < len(words[i]) and j < len(words[i+1]) and words[i][j] == words[i+1][j]:
                j += 1
            if j < len(words[i]) and j >= len(words[i+1]):
                return False
            if j < len(words[i]) and j < len(words[i+1]) and d[words[i][j]] > d[words[i+1][j]]:
                return False

        return True
        
sol = Solution()
print(sol.isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"))
        