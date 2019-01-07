# 942. DI String Match
class Solution:
    def diStringMatch(self, S):
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

sol = Solution()
print(sol.diStringMatch("IDID"))
print(sol.diStringMatch("III"))
print(sol.diStringMatch("DDI"))

            
            
        