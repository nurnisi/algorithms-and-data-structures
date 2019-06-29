# 556. Next Greater Element III
class Solution:
    def nextGreaterElement2(self, n: int) -> int:
        s = list(str(n))
        i = len(s)-2
        while i >= 0 and s[i] >= s[i+1]:
            i -= 1
        if i < 0: return -1
        
        j = i + 1
        for k in range(i+1, len(s)):
            if s[k] > s[i] and s[k] < s[j]:
                j = k

        s[i], s[j] = s[j], s[i]
        return int("".join(s[:i+1] + sorted(s[i+1:])))

    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        i, j = len(digits)-2, len(digits)-1

        while i >= 0 and digits[i] >= digits[i+1]:
            i -= 1
        
        if i == -1: return -1

        while digits[j] <= digits[i]:
            j -= 1

        digits[i], digits[j] = digits[j], digits[i]
        res = int("".join(digits[:i+1] + digits[i+1:][::-1]))

        if res >= 2**31 or res == n: return -1
        return res


# print(Solution().nextGreaterElement(12))
# print(Solution().nextGreaterElement(21))
print(Solution().nextGreaterElement(12222333))