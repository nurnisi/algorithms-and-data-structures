# 938. Range Sum of BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans = 0
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        def dfs(root):
            if root:
                if L <= root.val <= R: self.ans += root.val
                if L <= root.val: dfs(root.left)
                if R >= root.val: dfs(root.right)
        
        dfs(root)
        return self.ans