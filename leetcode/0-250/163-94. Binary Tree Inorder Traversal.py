# 94. Binary Tree Inorder Traversal
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # recursive
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        
        def helper(root):
            if root.left: helper(root.left)
            ans.append(root.val)
            if root.right: helper(root.right)
                
        if root: helper(root)
        return ans

    # iterative
    def inorderTraversal2(self, root):
        stack, ans = [], []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            ans.append(curr.val)
            curr = curr.right
        
        return ans
    

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(sol.inorderTraversal2(root))
