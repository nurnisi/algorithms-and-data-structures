# 173. Binary Search Tree Iterator
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# postorder
class BSTIterator:

    def __init__(self, root):
        self.root = root
        self.inorder(root)

    def inorder(self, root):
        if not root: return
        self.inorder(root.right)
        self.stack.append(root.val)
        self.inorder(root.left)

    def next(self):
        return self.stack.pop()

    def hasNext(self):
        return len(self.stack)
        
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()