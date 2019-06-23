# 1022. Sum of Root To Leaf Binary Numbers
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf2(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root, '')
        return self.ans
        
    def dfs(self, root, cur):
        cur += str(root.val)
        if not root.left and not root.right:
            self.ans += int(cur, 2)
            return

        if root.left: self.dfs(root.left, cur)
        if root.right: self.dfs(root.right, cur)

    def sumRootToLeaf(self, root: TreeNode, val=0) -> int:
        if not root: return 0
        val = val * 2 + root.val
        if not root.left and not root.right: return val
        return self.sumRootToLeaf(root.left, val) + self.sumRootToLeaf(root.right, val)
        