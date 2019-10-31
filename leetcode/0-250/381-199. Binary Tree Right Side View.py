# 199. Binary Tree Right Side View
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        out = []
        queue = collections.deque([root])
        
        while queue:
            out.append(queue[-1].val)
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        
        return out