# 230. Kth Smallest Element in a BST
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # inorder traversal: recursive
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        arr = []
        def helper(node):
            if node.left: helper(node.left)
            arr.append(node.val)
            if node.right: helper(node.right)
        
        helper(root)
        return arr[k-1]
    
    # iterative
    def kthSmallest2(self, root, k):
        cur, stack, res= root, [], []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if not k: return cur.val
            cur = cur.right

sol = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
print(sol.kthSmallest2(root, 3))
        

