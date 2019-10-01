# 1161. Maximum Level Sum of a Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def maxLevelSum2(self, root: TreeNode) -> int:
        queue = collections.deque([root])
        max_lvl = max_val = 0
        cur_lvl = 1
        
        while queue:
            size = len(queue)
            cur_val = 0
            for _ in range(size):
                node = queue.popleft()
                cur_val += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if cur_val > max_val:
                max_val = cur_val
                max_lvl = cur_lvl
            cur_lvl += 1
        
        return max_lvl

    def maxLevelSum(self, root: TreeNode) -> int:
        levels = [0]
        def dfs(node, lvl):
            if node:
                if lvl >= len(levels):
                    levels.append(0)
                levels[lvl] += node.val
                dfs(node.left, lvl+1)
                dfs(node.right, lvl+1)
        
        dfs(root, 1)
        return levels.index(max(levels))
        