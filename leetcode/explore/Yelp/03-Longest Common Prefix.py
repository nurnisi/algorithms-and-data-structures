# Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        match = strs[0]
        
        for s in strs:
            temp = []
            for a, b in zip(match, s):
                if a != b:
                    break
                temp.append(a)
            match = temp
                
        return ''.join(match)