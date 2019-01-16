# 701. Insert into a Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # recursive
    def insertIntoBST2(self, root, val):
        if not root:
            node = TreeNode(val)
            return node
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

    # recursive 2
    def insertIntoBST3(self, root, val):
        if not root: return TreeNode(val)
        if root.val > val: root.left = self.insertIntoBST(root.left, val)
        else: root.right = self.insertIntoBST(root.right, val)
        return root

    # iterative
    def insertIntoBST(self, root, val):
        node = prev = root
        while node:
            prev = root
            if node.val > val: node = node.left
            else: node = node.right
        if prev.val > val: prev.left = TreeNode(val)
        else: prev.right = TreeNode(val)
        return root

        
            

        