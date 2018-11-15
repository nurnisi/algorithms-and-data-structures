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

    # divide and conquer
    def longestCommonPrefix2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        return self.divideAndConquer(strs, 0, len(strs) - 1)
        
    def divideAndConquer(self, strs, left, right):
        if right == left:
            return strs[left]
        else:
            mid = (right + left) // 2
            leftRet = self.divideAndConquer(strs, left, mid)
            rightRet = self.divideAndConquer(strs, mid + 1, right)
            return self.check(leftRet, rightRet)

    def check(self, str1, str2):
        i, l1, l2 = 0, len(str1), len(str2)
        while i < l1 and i < l2 and str1[i] == str2[i]:
            i += 1
        return str1[:i]

class Trie(object):
    def __init__(self, )

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

