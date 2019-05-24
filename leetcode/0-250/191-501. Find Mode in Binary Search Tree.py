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

    # O(1) space
    def findMode2(self, root):
        self.modes = None
        self.curVal = self.curCount = self.maxCount = self.modeCount = 0
        self.inorder(root)
        self.modes = [0] * self.modeCount
        self.modeCount = self.curCount = 0
        self.inorder(root)
        return self.modes

    def handle(self, val):
        if val != self.curVal:
            self.curVal = val
            self.curCount = 0
        self.curCount += 1
        if self.curCount > self.maxCount:
            self.maxCount = self.curCount
            self.modeCount = 1
        elif self.curCount == self.maxCount:
            if self.modes: self.modes[self.modeCount] = self.curVal
            self.modeCount += 1
    
    def inorder(self, node):
        if not node: return
        self.inorder(node.left)
        self.handle(node.val)
        self.inorder(node.right)


root = TreeNode(4)
# root.left = TreeNode(2)
# root.right = TreeNode(6)
# root.left.left = TreeNode(2)
# root.left.right = TreeNode(2)
# root.right.left = TreeNode(5)
# root.right.right = TreeNode(7)
sol = Solution()
print(sol.findMode2(root))
        