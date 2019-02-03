# 865. Smallest Subtree with all the Deepest Nodes
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Solution:
    def subtreeWithAllDeepest2(self, root):
        def helper(root):
            if not root: return (None, 0)
            left, lc = helper(root.left)
            right, rc = helper(root.right)
            if lc > rc: return (left, lc + 1)
            elif lc < rc: return (right, rc + 1)
            else: return (root, rc + 1)
        return helper(root)[0]

    # with nametuple
    def subtreeWithAllDeepest(self, root):
        Result = collections.namedtuple("Result", "node dist")
        def helper(root):
            if not root: return Result(None, 0)
            L, R = helper(root.left), helper(root.right)
            if L.dist > R.dist: return Result(L.node, L.dist + 1)
            if R.dist > L.dist: return Result(R.node, R.dist + 1)
            return Result(root, L.dist + 1)
        return helper(root).node
        