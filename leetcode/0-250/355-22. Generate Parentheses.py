# 22. Generate Parentheses
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.dfs(n, '', 0, ans)
        return ans
        
    def dfs(self, n, pars, valid, ans):
        if len(pars) == n*2:
            if valid == 0:
                ans.append(pars)
            return
        
        if valid < n:
            self.dfs(n, pars + '(', valid + 1, ans)
        if valid > 0:
            self.dfs(n, pars + ')', valid - 1, ans)