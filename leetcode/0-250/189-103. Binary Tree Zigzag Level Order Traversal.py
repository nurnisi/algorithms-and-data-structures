# 103. Binary Tree Zigzag Level Order Traversal
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root):
        if not root: return []
        ans, queue, flag = [], deque(), 0
        queue.append(root)
        while queue:
            size, level = len(queue), []
            for _ in range(size):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                level.append(node.val)
            
            if flag: ans.append(list(reversed(level)))
            else: ans.append(level)
            flag ^= 1

        return ans

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
sol = Solution()
print(sol.zigzagLevelOrder(root))

                    



            


        