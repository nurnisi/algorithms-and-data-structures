# 113. Path Sum II
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        ans, stack = [], []
        def dfs(node, cursum):
            if not node: return
            stack.append(node.val)
            if not node.left and not node.right and cursum + node.val == sum:
                ans.append(stack.copy())
            dfs(node.left, cursum + node.val)
            dfs(node.right, cursum + node.val)
            stack.pop()
        dfs(root, 0)
        return ans

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
sol = Solution()
print(sol.pathSum(root, 8))
                    
                    
        