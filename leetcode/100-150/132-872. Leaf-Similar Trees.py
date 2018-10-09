#872. Leaf-Similar Trees
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

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

    
    def leafSimilar2(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        list1, list2 = [], []
        stack = [] 

        stack.append(root1)
        while stack != []:
            node = stack.pop()
            if node is None: break
            if node.left is not None: stack.append(node.left)
            if node.right is not None: stack.append(node.right)
            if node.left is None and node.right is None: list1.append(node.val)

        stack.append(root2) 
        while stack != []:
            node = stack.pop()
            if node is None: break
            if node.left is not None: stack.append(node.left)
            if node.right is not None: stack.append(node.right)
            if node.left is None and node.right is None: list2.append(node.val)

        return list1 == list2

    def leafSimilar3(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        list1, list2 = [], []
        if root1 is not None: self.helper3(root1, list1)
        if root2 is not None: self.helper3(root2, list2)
        return list1 == list2

    def helper3(self, root, list):
        stack = []
        stack.append(root)
        while stack != []:
            node = stack.pop()
            if node.left is not None: stack.append(node.left)
            if node.right is not None: stack.append(node.right)
            if node.left is None and node.right is None: list.append(node.val)