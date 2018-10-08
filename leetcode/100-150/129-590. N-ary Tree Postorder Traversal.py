"""
# Definition for a Node.
"""
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def postorder(self, root):
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

        for i in root.children:
            Solution.helper(self, i, list)

        list.append(root.val)
        