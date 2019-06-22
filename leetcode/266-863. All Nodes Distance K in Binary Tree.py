# 863. All Nodes Distance K in Binary Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Solution:
    def distanceK2(self, root, target, K):
        self.path = []
        self.found = False
        def findPath(node):
            if self.found or not node: return
            if node == target:
                self.found = True
                self.pathCopy = self.path.copy()
                return
            self.path.append(node)
            findPath(node.left)
            findPath(node.right)
            self.path.pop()
            
        findPath(root)
        self.pathCopy.append(target)
        
        ans = []
        
        def dfs(node, k):
            if not node or k < 0: return
            if k == 0:
                ans.append(node.val)
                return
            dfs(node.left, k-1)
            dfs(node.right, k-1)
        
        prev = None
        while self.pathCopy:
            cur = self.pathCopy.pop()
            if cur.left and prev != cur.left:
                dfs(cur.left, K - 1)
            if cur.right and prev != cur.right:
                dfs(cur.right, K - 1)
            if K == 0:
                ans.append(cur.val)
            K -= 1
            prev = cur
            
        return ans

    def distanceK3(self, root, target, K):
        self.path = []
        self.found = False

        def findPath(node):
            if self.found or not node: return
            if node == target:
                self.found = True
                return
            self.path.append(node)
            findPath(node.left)
            findPath(node.right)
            if not self.found: self.path.pop()
            
        findPath(root)

        self.path.append(target)
        ans, visited = [], set()
        
        def dfs(node, k):
            if node in visited or not node or k < 0: return
            if k == 0:
                ans.append(node.val)
                return
            dfs(node.left, k-1)
            dfs(node.right, k-1)
        
        while self.path:
            cur = self.path.pop()
            dfs(cur, K)
            visited.add(cur)
            K -= 1
            
        return ans

    def distanceK(self, root, target, K):
        def dfs(node, par = None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)
                
        dfs(root)
        seen = {target}
        
        queue = collections.deque([(target, 0)])
        while queue:
            if queue[0][1] == K:
                return [node.val for node, _ in queue]
            node, d = queue.popleft()
            for nei in [node.left, node.right, node.par]:
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, d + 1))
                    
        return []

root = TreeNode(0)

root.left = TreeNode(1)

root.left.left = TreeNode(3)
root.left.right = TreeNode(2)

print(Solution().distanceK(root, root.left.right, 1))

root = TreeNode(3)

root.left = TreeNode(5)
root.right = TreeNode(1)

root.left.left = TreeNode(6)
root.left.right = TreeNode(2)

root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

print(Solution().distanceK(root, root.left, 2))