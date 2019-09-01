# 301. Remove Invalid Parentheses
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans = []
        self.helper('', 0, 0, len(s), ans, s)
        return set(ans)
        
    def helper(self, pars, i, valid, n, ans, s):
        if i == n:
            if valid == 0:
                ans.append(pars)
        else:
            if s[i] == '(':
                self.helper(pars+s[i], i+1, valid+1, n, ans, s)
                if not ans or n-len(ans[0]) >= i-len(pars)+1:
                    self.helper(pars, i+1, valid, n, ans, s)
            elif s[i] == ')':
                if valid != 0:
                    self.helper(pars+s[i], i+1, valid-1, n, ans, s)
                if not ans or n-len(ans[0]) >= i-len(pars)+1:
                    self.helper(pars, i+1, valid, n, ans, s)
            else:
                self.helper(pars+s[i], i+1, valid, n, ans, s)