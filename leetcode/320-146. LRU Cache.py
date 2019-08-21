# 146. LRU Cache
class LRUCache2:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.queue = collections.deque()

    def get(self, key: int) -> int:
        if key in self.d:
            if key in self.queue:
                self.queue.remove(key)
            self.queue.append(key)
            return self.d[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.d and len(self.d) == self.capacity:
            self.d.pop(self.queue.popleft())
            
        self.d[key] = value
        if key in self.queue:
            self.queue.remove(key)
        self.queue.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class LRUCache:

    def __init__(self, capacity: int):
        self.d = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        v = self.d.pop(key)
        self.d[key] = v
        return v

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d.pop(key)
        elif len(self.d) == self.capacity:
            self.d.popitem(last=False)
        self.d[key] = value