# 968. Binary Tree Cameras
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans = 0
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node: return 2
            if not node.left and not node.right: return 0
            l, r = dfs(node.left), dfs(node.right)
            if l == 0 or r == 0:
                self.ans += 1
                return 1
            if l == 1 or r == 1:
                return 2
            return 0

        return (dfs(root) == 0) + ans
                
        