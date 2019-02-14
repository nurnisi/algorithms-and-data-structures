# 572. Subtree of Another Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: 'TreeNode', t: 'TreeNode') -> 'bool':
        if not s: return False
        if s.val != t.val: return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        return self.checkSubtree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def checkSubtree(self, s, t):
        if not s and not t: return True
        if not s or not t: return False
        if s.val != t.val: return False
        return self.checkSubtree(s.left, t.left) and self.checkSubtree(s.right, t.right)