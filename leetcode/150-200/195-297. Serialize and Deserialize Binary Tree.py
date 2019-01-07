# 297. Serialize and Deserialize Binary Tree
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
# TLE: 47/48
class Codec2:
    def serialize(self, root):
        levels = self.dfs(root)
        arr = []
        queue = deque([root])
        while queue and levels:
            s = len(queue)
            for i in range(s):
                node = queue.popleft()
                arr.append(str(node.val) if node else "null")
                queue.append(node.left if node else None)
                queue.append(node.right if node else None)
            levels -= 1
        return ','.join(arr)
    
    def dfs(self, root):
        if not root: return 0
        return 1 + max(self.dfs(root.left), self.dfs(root.right))

    def deserialize(self, data):
        if not data: return None
        arr = data.split(',')
        root = TreeNode(int(arr[0]))
        queue = deque([root])
        i = 1
        while i < len(arr):
            node = queue.popleft()
            left = right = None
            if arr[i] != 'null':
                left = TreeNode(arr[i])
                node.left = left
            if arr[i+1] != 'null':
                right = TreeNode(arr[i+1])
                node.right = right
            queue.append(left)
            queue.append(right)
            i += 2
        return root

class Codec:
    def serialize(self, root):
        arr = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                arr.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else: arr.append('null')
        return ','.join(arr)
    
    def deserialize(self, data):
        if not data or data == 'null': return None
        arr = data.split(',')
        root = TreeNode(arr[0])
        queue = deque([root])
        i, n = 0, len(arr)
        while queue and i < n:
            node = queue.popleft()
            if i+1 < n and arr[i+1] != 'null':
                left = TreeNode(arr[i+1])
                node.left = left
                queue.append(left)
            if i+2 < n and arr[i+2] != 'null':
                right = TreeNode(arr[i+2])
                node.right = right
                queue.append(right)
            i += 2
        return root

# Your Codec object will be instantiated and called as such:
root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
root.right.left.left = TreeNode(3)
root.right.left.right = TreeNode(1)

codec = Codec()
# print(codec.serialize(None))
print(codec.deserialize(codec.serialize(root)))
# print(codec.serialize(codec.deserialize(codec.serialize(root))))