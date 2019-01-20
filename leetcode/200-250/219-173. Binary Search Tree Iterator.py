# 173. Binary Search Tree Iterator
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# postorder and stack
class BSTIterator2:

    def __init__(self, root):
        self.root = root
        self.stack = []
        self.inorder(root)

    def inorder(self, root):
        if not root: return
        self.inorder(root.right)
        self.stack.append(root.val)
        self.inorder(root.left)

    def next(self):
        return self.stack.pop()

    def hasNext(self):
        return len(self.stack) > 0

# inorder and queue 
from collections import deque
class BSTIterator3:

    def __init__(self, root):
        self.root = root
        self.queue = deque()
        self.inorder(root)

    def inorder(self, root):
        if not root: return
        self.inorder(root.left)
        self.queue.append(root.val)
        self.inorder(root.right)

    def next(self):
        return self.queue.popleft()

    def hasNext(self):
        return len(self.queue) > 0

# O(h) space complexity
class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self.populate(root)

    def populate(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        node = self.stack.pop()
        self.populate(node.right)
        return node.val
        
    def hasNext(self):
        return len(self.stack) > 0
        
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()