# 942. DI String Match
class Solution:
    def diStringMatch2(self, S):
        ans, inc, dec = [0], 1, -1
        for c in S:
            if c == 'I':
                ans.append(inc)
                inc += 1
            else:
                ans.append(dec)
                dec -= 1
        
        for i in range(len(ans)):
            ans[i] -= dec + 1

        return ans

    def diStringMatch(self, S):
        lo, hi = 0, len(S)
        ans = []
        for c in S:
            if c == 'I':
                ans.append(lo)
                lo += 1
            else:
                ans.append(hi)
                hi -= 1
        return ans + [lo]

sol = Solution()
print(sol.diStringMatch("IDID"))
print(sol.diStringMatch("III"))
print(sol.diStringMatch("DDI"))

            
            
        