# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        if inorder:
            ix = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ix])
            root.left = self.buildTree(preorder, inorder[:ix])
            root.right = self.buildTree(preorder, inorder[ix + 1:])
            return root

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode(2)
root.left.right = TreeNode(1)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
sol = Solution()
sol.buildTree([3,9,20,15,7], [9,3,15,20,7])
# sol.buildTree([3,9,2,1,20,15,7], [2,9,1,3,15,20,7])



            

        