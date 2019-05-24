# 953. Verifying an Alien Dictionary
class Solution:
    def isAlienSorted2(self, words, order):
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

    def isAlienSorted(self, words, order):
        d = {c: i for i, c in enumerate(order)}
        for i in range(len(words)-1):
            w1, w2, flag = words[i], words[i+1], True
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if d[w1[j]] > d[w2[j]]: return False
                    flag = False
                    break
            if flag and len(w1) > len(w2): return False
        return True


sol = Solution()
print(sol.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"))
print(sol.isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"))
print(sol.isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"))
        