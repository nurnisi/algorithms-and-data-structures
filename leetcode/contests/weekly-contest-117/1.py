# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node, val):
            if not node:
                return True
            if node.val != val:
                return False
            return helper(node.left, val) and helper(node.right, val)
        
        return helper(root, root.val)
            
        