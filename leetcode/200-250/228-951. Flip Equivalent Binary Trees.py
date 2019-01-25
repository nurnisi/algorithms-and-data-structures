# 951. Flip Equivalent Binary Trees
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import itertools
class Solution:
    def flipEquiv2(self, root1, root2):
        if not root1 and not root2: return True
        if not root1 or not root2: return False
        
        r1left = root1.left.val if root1.left else None
        r1right = root1.right.val if root1.right else None
        r2left = root2.left.val if root2.left else None
        r2right = root2.right.val if root2.right else None

        if r1left == r2left and r1right == r2right:
            return self.flipEquiv(root1.left, root2.left) and \
                    self.flipEquiv(root1.right, root2.right)
        elif r1left == r2right and r1right == r2left:
            return self.flipEquiv(root1.left, root2.right) and \
                    self.flipEquiv(root1.right, root2.left)
        return False

    # leetcode: recursive
    def flipEquiv3(self, root1, root2):
        if not root1 and not root2: return True
        if not root1 or not root2 or root1.val != root2.val: return False
        
        return (self.flipEquiv(root1.left, root2.left) and 
                self.flipEquiv(root1.right, root2.right) or
                self.flipEquiv(root1.left, root2.right) and
                self.flipEquiv(root1.right, root2.left))

    # leetcode: canonical traversal
    def flipEquiv(self, root1, root2):
        def dfs(node):
            if node:
                yield node.val
                L = node.left.val if node.left else -1
                R = node.right.val if node.right else -1
                if L < R:
                    yield from dfs(node.left)
                    yield from dfs(node.right)
                else:
                    yield from dfs(node.right)
                    yield from dfs(node.left)
                yield '#'
        
        return all(x == y for x, y in itertools.zip_longest(dfs(root1), dfs(root2)))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(8)

sol = Solution()
sol.flipEquiv(root, root)


        
        