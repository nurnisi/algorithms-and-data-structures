#589. N-ary Tree Preorder Traversal

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        list = []
        Solution.helper(self, root, list)
        return list

    def helper(self, root, list):
        if root == None:
            return
        
        list.append(root.val)
        for node in root.children:
            Solution.helper(self, node, list)

    def preorder2(self, root):
        if root == None:
            return []
        
        stack, list = [], []
        stack.append(root)
        while len(stack) != 0:
            node = stack.pop()
            list.append(node.val)
            for i in reversed(node.children):
                stack.append(i)

        return list