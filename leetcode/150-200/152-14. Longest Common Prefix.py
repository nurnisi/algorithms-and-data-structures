# 14. Longest Common Prefix
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        cm = strs[0]
        tail = len(cm)
        for i in range(1, len(strs)):
            s = strs[i]
            i = 0
            while i < len(cm) and i < len(s) \
                  and i < tail and cm[i] == s[i]:
                i += 1
            tail = i
        return cm[:tail]

