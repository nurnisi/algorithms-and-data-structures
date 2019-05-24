#559. Maximum Depth of N-ary Tree

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

def maxDepth(root):
    """
    :type root: Node
    :rtype: int
    """
    if root == None:
        return 0
    return helper(root, 1)

def helper(root, length):
    locLength = length
    for i in root.children:
        locLength = max(helper(i, length + 1), locLength)

    return locLength

ll = Node(5, [])
lr = Node(6, [])
l = Node(3, [ll, lr])
m = Node(2, [])
r = Node(4, []) 
root = Node(1, [l, m, r])
print(maxDepth(root))

def maxDepth2(self, root):
    if root == None:
        return 0
    elif root.children == []:
        return 1
    else:
        heights = [self.maxDepth2(c) for c in root.children]
        return max(heights) + 1

def maxDepth3(self, root):
    stack = []
    if root is not None:
        stack.append((1, root))
    
    depth = 0
    while stack != []:
        curDepth, root = stack.pop()
        depth = max(depth, curDepth)
        for c in root.children:
            stack.append((curDepth + 1, c))

    return depth