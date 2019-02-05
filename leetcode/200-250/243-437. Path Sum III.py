# 437. Path Sum III
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum2(self, root, sum):
        sums = []
        self.cnt = 0
        
        def helper(root):
            if not root: return
            for i in range(len(sums)):
                sums[i] += root.val
                if sums[i] == sum:
                    self.cnt += 1
                    
            if root.val == sum: self.cnt += 1
            sums.append(root.val)
            helper(root.left)
            helper(root.right)
            sums.pop()
            for i in range(len(sums)):
                sums[i] -= root.val  
        
        helper(root)
        return self.cnt

    def pathSum(self, root, sum):
        self.sums = []

        def helper(root):
            if not root: return 0
            self.sums = list(map(lambda x: x + root.val, self.sums))
            self.sums.append(root.val)
            cnt = self.sums.count(sum)

            cnt += helper(root.left)
            cnt += helper(root.right)
            self.sums.pop()
            self.sums = list(map(lambda x: x - root.val, self.sums))

            return cnt
    
        return helper(root)

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(1)
root.right.right = TreeNode(11)

sol = Solution()
print(sol.pathSum(root, 8))