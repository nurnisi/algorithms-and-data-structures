# 125. Valid Palindrome
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j, sLow = 0, len(s) - 1, s.lower()
        while i < j:
            while not sLow[i].isalnum() and i < j: i += 1
            while not sLow[j].isalnum() and i < j: j -= 1
            if sLow[i] != sLow[j]:
                return False
            i += 1
            j -= 1
        return True