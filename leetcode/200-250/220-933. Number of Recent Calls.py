# 933. Number of Recent Calls
from collections import deque
class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t):
        self.queue.append(3000 + t)
        while self.queue and self.queue[0] - t < 0:
            self.queue.popleft()
        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)