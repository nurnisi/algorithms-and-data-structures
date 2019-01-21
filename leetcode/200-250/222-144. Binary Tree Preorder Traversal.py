# 144. Binary Tree Preorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive
class Solution2:
    def preorderTraversal(self, root):
        self.ans = []
        self.preorder(root)
        return self.ans

    def preorder(self, root):
        if not root: return
        self.ans.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

# iterative
class Solution3:
    def preorderTraversal(self, root):
        ans, stack = [], [root]
        while stack:
            node = stack.pop()
            if not node: continue
            stack.append(node.right)
            stack.append(node.left)
            ans.append(node.val)
        return ans

# morris travel
class Solution:
    def preorderTraversal(self, root):
        node, output = root, []

        while node:
            if not node.left:
                output.append(node.val)
                node = node.right
            else:
                predecessor = node.left

                while predecessor.right and predecessor.right is not node:
                    predecessor = predecessor.right
                
                if not predecessor.right:
                    output.append(node.val)
                    predecessor.right = node
                    node = node.left
                else:
                    predecessor.right = None
                    node = node.right

        return output