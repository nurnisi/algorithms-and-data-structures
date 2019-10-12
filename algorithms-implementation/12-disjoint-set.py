class Node:
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.rank = 0

class DisjointSet:
    def __init__(self, nums):
        self.map = {}
        self.makeSet(nums)

    def makeSet(self, nums):
        for n in nums: 
            self.map[n] = Node(n)

    def union(self, val1, val2):
        parent1 = self.findSet(val1)
        parent2 = self.findSet(val2)

        if parent1 == parent2: return

        if parent1.rank >= parent2.rank:
            if parent1.rank == parent2.rank:
                parent1.rank += 1
            parent2.parent = parent1
        else:
            parent1.parent = parent2

    def findSet(self, val):
        return self.findSetHelper(self.map[val])

    def findSetHelper(self, node):
        if node == node.parent:
            return node
        node.parent = self.findSetHelper(node.parent)
        return node.parent

# test
ds = DisjointSet(range(1,8))

ds.union(1, 2)
ds.union(2, 3)
ds.union(4, 5)
ds.union(6, 7)
ds.union(5, 6)
ds.union(3, 7)

for x in range(1,8):
    print(ds.findSet(x).val)

    