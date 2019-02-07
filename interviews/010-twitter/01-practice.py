import heapq
class TreeNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # comparator
    def __lt__(self, other):
        return self.freq < other.freq

class Huffman:
    def __init__(self, charToFreq):
        # heap
        self.nodes = [TreeNode(char, freq) for char, freq in charToFreq]
        heapq.heapify(self.nodes)

        # root
        self.root = self.getRoot()

        # encoding
        self.encoding = []
        self.dfs(self.root, [])

    def getRoot(self):
        while len(self.nodes) > 1:
            node1, node2 = heapq.heappop(self.nodes), heapq.heappop(self.nodes)
            inter = TreeNode(None, node1.freq + node2.freq)
            inter.left, inter.right = node1, node2
            heapq.heappush(self.nodes, inter)
        return heapq.heappop(self.nodes)

    def dfs(self, node, arr):
        if not node: return
        if not node.left and not node.right:
            self.encoding.append((node.char, arr))
        
        self.dfs(node.left, arr + [0])
        self.dfs(node.right, arr + [1])
        
huff = Huffman([('b', 9), ('d', 13), ('c', 12), ('e', 16), ('f', 45), ('a', 5)])
