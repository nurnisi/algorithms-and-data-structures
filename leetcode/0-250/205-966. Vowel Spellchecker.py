# 966. Vowel Spellchecker
import collections
class Solution:
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        setWL = set(wordlist)
        
        dictCap = {}
        for word in wordlist:
            if word.lower() not in dictCap:
                dictCap[word.lower()] = word

        vowels = ('a', 'e', 'i', 'o', 'u')
        dictVow = {}
        for word in wordlist:
            tmpWord = word.lower()
            for v in vowels:
                tmpWord = tmpWord.replace(v, '#')
            if tmpWord.lower() not in dictVow:
                dictVow[tmpWord.lower()] = word

        # print(setWL)
        # print(dictCap)
        # print(dictVow)

        ans = []
        for q in queries:
            if q in setWL:
                ans.append(q)
            elif q.lower() in dictCap:
                ans.append(dictCap[q.lower()])
            else:
                tmpWord = q.lower()
                for v in vowels:
                    tmpWord = tmpWord.replace(v, '#')
                if tmpWord.lower() in dictVow:
                    ans.append(dictVow[tmpWord.lower()])
                else:
                    ans.append("")
        
        return ans



        
sol = Solution()
print(sol.spellchecker(["KiTe","kite","hare","Hare"], ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]))
print(sol.spellchecker(["YellOw"], ["yollow"]))

