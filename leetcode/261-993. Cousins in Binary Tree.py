# 993. Cousins in Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def isCousins2(self, root: TreeNode, x: int, y: int) -> bool:
        queue = deque([(root, None)])
        
        while queue:
            ln = len(queue)
            xPar = yPar = None
            for _ in range(ln):
                (cur, parent) = queue.popleft()
                if cur.left: queue.append((cur.left, cur))
                if cur.right: queue.append((cur.right, cur))
                if cur.val == x: xPar = parent
                if cur.val == y: yPar = parent
            if xPar and yPar and xPar != yPar: return True
            if xPar or yPar: return False
        
        return False
    
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        depth, parent = {}, {}
        def dfs(node, par = None):
            if node:
                depth[node.val] = depth[par.val] + 1 if par else 0
                parent[node.val] = par
                dfs(node.left, node)
                dfs(node.right, node)
        
        dfs(root)
        return depth[x] == depth[y] and parent[x] != parent[y]