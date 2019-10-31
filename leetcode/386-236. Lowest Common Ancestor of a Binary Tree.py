# 236. Lowest Common Ancestor of a Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        
        def helper(node):
            if not node or self.ans:
                return False
            
            left = helper(node.left)
            right = helper(node.right)
            mid = node == p or node == q
            
            if not self.ans and sum([mid, left, right]) >= 2:
                    self.ans = node
            
            return mid or left or right
        
        helper(root)
        return self.ans