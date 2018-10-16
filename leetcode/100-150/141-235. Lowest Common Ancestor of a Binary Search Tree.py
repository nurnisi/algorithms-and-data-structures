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
        
        left = self.lowestCommonAncestor(root, p, q)
        right = self.lowestCommonAncestor(root, p, q)
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

    def lowestCommonAncestor2(self, root, p, q):
        if not root:
            return None
        
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor2(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor2(root.right, p, q)
        return root

    def lowestCommonAncestor3(self, root, p, q):
        while root:
            if p.val < root.val > q.val:
                root = root.left
            elif p.val > root.val < q.val:
                root = root.right
            else:
                return root

    def lowestCommonAncestor4(self, root, p, q):
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor4(root.left, p, q)
        elif p.val > root.val < q.val:
            return self.lowestCommonAncestor4(root.right, p, q)
        return root

    def lowestCommonAncestor5(self, root, p, q):
        a, b = sorted([p.val, q.val])
        while not a <= root.val <= b:
            root = (root.left, root.right)[a > root.val]
        return root

    def lowestCommonAncestor6(self, root, p, q):
        next = p.val < root.val > q.val and root.left or \
               p.val > root.val < q.val and root.right
        return self.lowestCommonAncestor6(next, p, q) if next else root

    def lowestCommonAncestor7(self, root, p, q):
        return root if (root.val - p.val) * (root.val - q.val) < 1  \
               else self.lowestCommonAncestor7((root.left, root.right)[p.val > root.val], p, q)


    

    
                



        

        