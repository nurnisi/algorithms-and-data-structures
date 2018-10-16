# 235. Lowest Common Ancestor of a Binary Search Tree
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        left = self.helper(root, p, q)
        right = self.helper(root, p, q)
        if left and right:
            return root
        node = None
        if (root.val == p.val or root.val == q.val):
            node = root
        if (node and left) or (node and right):
            return root
        if left:
            return left
        if right:
            return right
        return node



        

        