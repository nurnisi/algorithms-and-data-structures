# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flipMatchVoyage2(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        ans, lenv = [], len(voyage)
        def preorder(node, i):
            if not node: return True
            left = right = None
            if node.left: left = node.left.val
            if node.right: right = node.right.val
            
            lv = rv = None
            if 2*i+1 < lenv: lv = voyage[2*i+1]
            if 2*i+2 < lenv: rv = voyage[2*i+2]
            if left == lv and right == rv:
                return preorder(node.left, 2*i+1) and preorder(node.right, 2*i+2)
            elif left == rv and right == lv:
                ans.append(node.val)
                return preorder(node.right, 2*i+1) and preorder(node.left, 2*i+2)
            return False

        if preorder(root, 0): return ans
        return [-1]

    def flipMatchVoyage3(self, root, voyage):
        ans, lenv = [], len(voyage)
        def preorder(node, i):
            if not node: return True
            left = right = None
            if node.left: left = node.left.val
            if node.right: right = node.right.val
            
            lv = rv = None
            if 2*i+1 < lenv: lv = voyage[2*i+1]
            if 2*i+2 < lenv: rv = voyage[2*i+2]

            if left and right and left == lv and right == rv:
                return preorder(node.left, 2*i+1) and preorder(node.right, 2*i+2)
            elif left and right and left == rv and right == lv:
                ans.append(node.val)
                return preorder(node.right, 2*i+1) and preorder(node.left, 2*i+2)
            return False

        if preorder(root, 0): return ans
        return [-1]

    def flipMatchVoyage(self, root, voyage):
        vtree = self.makeTree(voyage, 0)

        def preorder2(self, rnode, vnode, ans):
        if not rnode and not vnode: return
        
        self.preorder2(node.left)
        self.preorder2(node.right)

        self.preorder2(vtree)

    def makeTree(self, voyage, i):
        if i >= len(voyage): return None
        root = TreeNode(voyage[i])
        root.left = self.makeTree(voyage, 2*i+1)
        root.right = self.makeTree(voyage, 2*i+2)
        return root

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
# root.left.left = TreeNode(2)
# root.left.right = TreeNode(2)
# root.right.left = TreeNode(5)
# root.right.right = TreeNode(7)
sol = Solution()
print(sol.flipMatchVoyage(root, [1,3,2])) 

