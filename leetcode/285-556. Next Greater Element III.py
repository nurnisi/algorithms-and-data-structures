# 556. Next Greater Element III
class Solution:
    def nextGreaterElement(self, n: int) -> int:
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

# print(Solution().nextGreaterElement(12))
# print(Solution().nextGreaterElement(21))
print(Solution().nextGreaterElement(12222333))