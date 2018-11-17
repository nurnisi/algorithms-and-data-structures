# 28. Implement strStr()
class Solution(object):
    # brute-force time limit exceeded
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lh , ln = len(haystack), len(needle)
        if ln == 0: return 0
        for i in range(lh):
            j = 0
            while i + j < lh and j < ln:
                if haystack[i + j] != needle[j]: break
                j += 1
            if j == ln:
                return i
        
        return -1