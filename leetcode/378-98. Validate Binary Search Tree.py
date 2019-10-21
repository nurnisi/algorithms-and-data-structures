# 98. Validate Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.flag = True
        
        def dfs(node):
            if not node:
                return (float('inf'), float('-inf'))
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left[1] != float('-inf'):
                self.flag = self.flag and left[1] < node.val
            if right[0] != float('inf'):
                self.flag = self.flag and right[0] > node.val
            
            return (min(left[0], node.val), max(right[1], node.val))
            
        dfs(root)
        return self.flag