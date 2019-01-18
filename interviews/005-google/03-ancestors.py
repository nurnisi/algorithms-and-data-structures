import collections
class Tree:
    def __init__(self, x):
        self.val = x
        self.children = []

def makeTree(node, d):
    if node and node.val in d:
        for c in d[node.val]:
            child = Tree(c)
            node.children.append(child)
            makeTree(child, d)

def ancestors(D, arr):
    n = len(arr)
    d = {}
    for i in range(n):
        d.setdefault(arr[i], []).append(i)

    root = Tree(0)
    makeTree(root, d)
    ans = [-1] * n
    dfs(root, [], ans, D)

    return ans

def dfs(node, stack, ans, D):
    if node:
        if len(stack) >= D:
            ans[node.val] = stack[-D]
        stack.append(node.val)
        for c in node.children:
            dfs(c, stack, ans, D)
        stack.pop()

print(ancestors(2, [-1,0,1,2,3]))
print(ancestors(3, [-1,0,4,2,1]))