# 1110. Delete Nodes And Return Forest
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ans = []
        def dfs(node):
            if node:
                ret = TreeNode(node.val)
                ret.left = dfs(node.left)
                ret.right = dfs(node.right)
                if node.val in to_delete:
                    if ret.left: ans.append(ret.left)
                    if ret.right: ans.append(ret.right)
                    return None
                return ret
                    
        ret = dfs(root)
        if ret and ret.val not in to_delete: ans.append(ret)
        return ans