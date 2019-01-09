# 114. Flatten Binary Tree to Linked List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        self.dfs(root)

    def dfs(self, node):
        if not node: return None
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        if not left and not right: 
            return (node, node)
        elif not right:
            node.left = None
            node.right = left[0]
            return (node, left[1])
        elif left and right:
            node.left = None
            node.right = left[0]
            left[1].right = right[0]
        return (node, right[1])

    def dfs2(self, node):
        if not node: return None
        left = self.dfs2(node.left)
        right = self.dfs2(node.right)
        
        if not left and not right: return node
        if left: 
            left.right = node.right
            node.right = node.left
            node.left = None
        if right: return right
        return left
        
        



        