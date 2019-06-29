# 116. Populating Next Right Pointers in Each Node
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        queue = deque([root])
        
        while queue:
            ln = len(queue)
            prev = None
            for _ in range(ln):
                cur = queue.popleft()
                if prev: prev.next = cur
                prev = cur
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
        
        return root