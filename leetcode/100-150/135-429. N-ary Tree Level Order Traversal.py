# 429. N-ary Tree Level Order Traversal

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

from collections import deque

def levelOrder(root):
    """
    :type root: Node
    :rtype: List[List[int]]
    """
    if root is None:
        return []

    queue = deque()
    ans = []
    queue.append(root)
    while queue:
        l = len(queue)
        arr = []
        for _ in range(l):
            node = queue.popleft()
            for c in node.children:
                queue.append(c)
            arr.append(node.val)
        ans.append(arr)
    
    return ans

ll = Node(5, [])
lr = Node(6, [])
l = Node(3, [ll, lr])
m = Node(2, [])
r = Node(4, []) 
root = Node(1, [l, m, r])
print(levelOrder(root))