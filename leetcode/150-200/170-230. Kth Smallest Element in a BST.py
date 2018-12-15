# 230. Kth Smallest Element in a BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        arr = []
        def helper(node):
            if node.left: helper(node.left)
            arr.append(node.val)
            if node.right: helper(node.right)
        
        helper(root)
        return arr[k-1]
            