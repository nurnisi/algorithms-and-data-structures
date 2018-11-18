# 28. Implement strStr()
class Solution(object):
    # brute-force 1
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lh , ln = len(haystack), len(needle)
        if ln == 0: return 0
        for i in range(lh - ln + 1):
            j = 0
            while j < ln:
                if haystack[i + j] != needle[j]: break
                j += 1
            if j == ln:
                return i
        
        return -1

    # brute-force 2
    def strStr1(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lh, ln = len(haystack), len(needle)
        for i in range(lh - ln + 1):
            if haystack[i : (i+ln)] == needle:
                return i
        return -1