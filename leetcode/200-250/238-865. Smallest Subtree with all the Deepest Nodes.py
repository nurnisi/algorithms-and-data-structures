# 865. Smallest Subtree with all the Deepest Nodes
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root):
        def helper(root):
            if not root: return (None, 0)
            left, lc = helper(root.left)
            right, rc = helper(root.right)
            if lc > rc: return (left, lc + 1)
            elif lc < rc: return (right, rc + 1)
            else: return (root, rc + 1)
        return helper(root)[0]
        