# 501. Find Mode in Binary Search Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        d = collections.defaultdict(int)
        def dfs(node):
            if node:
                d[node.val] += 1
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        m = max(d.values())
        ans = []
        for k, v in d.items():
            if v == m:
                ans.append(k)

        return ans
        

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
sol = Solution()
print(sol.findMode(root))
        