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

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class Node:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.d:
            n = self.d[key]
            self._remove(n)
            self._add(n)
            return n.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self._remove(self.d[key])
        n = Node(key, value)
        self._add(n)
        self.d[key] = n
        if len(self.d) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.d[n.key]
        
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = p
        
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)