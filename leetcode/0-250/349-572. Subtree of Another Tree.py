# 572. Subtree of Another Tree
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s: return self.isSubtree(s.left, t) or self.isSubtree(s.right, t) or self.dfs(s, t)
        return False
        
    def dfs(self, s, t):
        if not s and not t: return True
        if s and t and s.val == t.val:
            return self.dfs(s.left, t.left) and self.dfs(s.right, t.right)
        return False