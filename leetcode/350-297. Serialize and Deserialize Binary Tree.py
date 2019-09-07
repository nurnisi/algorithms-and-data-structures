# 297. Serialize and Deserialize Binary Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        q = collections.deque([root])
        ser = []
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                val = 'None'
                if node:
                    val = str(node.val)
                    q.append(node.left)
                    q.append(node.right)
                ser.append(val)
    
        return ','.join(ser)

    def deserialize(self, data):
        ser = collections.deque(data.split(','))
        if not ser or ser[0] == 'None': return None
        
        root = TreeNode(int(ser.popleft()))
        deser = collections.deque([root])
        
        while ser and deser:
            node = deser.popleft()
            left = ser.popleft()
            right = ser.popleft()
            if left != 'None':
                node.left = TreeNode(int(left))
                deser.append(node.left)
            if right != 'None':
                node.right = TreeNode(int(right))
                deser.append(node.right)
                
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))