# 66. Plus One
class Solution(object):
    def plusOne(self, digits):
        i, c = len(digits) - 1, 1
        while i >= 0:
            cur = digits[i] + c
            digits[i] = cur % 10
            c = cur / 10
            i -= 1
        if c: digits.insert(0, c)
        return digits

