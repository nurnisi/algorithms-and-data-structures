# 449. Serialize and Deserialize BST
# BFS
class Codec2:
    def serialize(self, root):
        arr = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                arr.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else: arr.append('null')
        return ','.join(arr)
    
    def deserialize(self, data):
        if not data or data == 'null': return None
        arr = data.split(',')
        root = TreeNode(arr[0])
        queue = deque([root])
        i, n = 0, len(arr)
        while queue and i < n:
            node = queue.popleft()
            if i+1 < n and arr[i+1] != 'null':
                left = TreeNode(arr[i+1])
                node.left = left
                queue.append(left)
            if i+2 < n and arr[i+2] != 'null':
                right = TreeNode(arr[i+2])
                node.right = right
                queue.append(right)
            i += 2
        return root