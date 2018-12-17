# 102. Binary Tree Level Order Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    # iterative
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        ans = []
        queue = deque([root])
        while queue:
            size = len(queue)
            level = []
            for i in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(level)
        return ans

    # recursive
    def levelOrder2(self, root):
        ans = []
        def helper(node, level):
            if level >= len(ans): ans.append([node.val])
            else: ans[level].append(node.val)
            if node.left: helper(node.left, level + 1)
            if node.right: helper(node.right, level + 1)
        
        if root: helper(root, 0)
        return ans
    