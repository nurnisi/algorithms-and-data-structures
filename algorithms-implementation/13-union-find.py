class UnionFind:
    def __init__(self, n):
        self.items = [set([i]) for i in range(n)]

    def find_index(self, item):
        for i, x in enumerate(self.items):
            if item in x:
                return i

    def union(self, a, b):
        ai = self.find_index(a)
        bi = self.find_index(b)

        if ai != bi:
            self.items[ai] += self.items[bi]
            self.items.pop(bi)
    


