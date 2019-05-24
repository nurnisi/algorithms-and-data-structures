# 17. Letter Combinations of a Phone Number
class Solution:
    d = {
        '2': ('a', 'b', 'c'),
        '3': ('d', 'e', 'f'),
        '4': ('g', 'h', 'i'),
        '5': ('j', 'k', 'l'),
        '6': ('m', 'n', 'o'),
        '7': ('p', 'q', 'r', 's'),
        '8': ('t', 'u', 'v'),
        '9': ('w', 'x', 'y', 'z')
    }
    def letterCombinations(self, digits):
        ans, n = [], len(digits)
        if not n: return ans

        def helper(i, arr):
            if i == n: 
                ans.append(''.join(arr))
                return
            for c in self.d[digits[i]]:
                helper(i+1, arr + [c])
        
        helper(0, [])
        return ans

sol = Solution()
print(sol.letterCombinations("235"))

        