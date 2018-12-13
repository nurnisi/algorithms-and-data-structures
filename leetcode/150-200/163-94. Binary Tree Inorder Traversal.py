# 94. Binary Tree Inorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        
        def helper(root):
            if root.left: helper(root.left)
            ans.append(root.val)
            if root.right: helper(root.right)
                
        if root: helper(root)
        return ans