#872. Leaf-Similar Trees
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        list1, list2 = [], []
        self.helper(root1, list1)
        self.helper(root2, list2)
        return list1 == list2

    def helper(self, root, list):
        if root is None:
            return
        if root.left == None and root.right == None:
            list.append(root.val)
        if root.left is not None:
            self.helper(root.left, list)
        if root.right is not None:
            self.helper(root.right, list)