# 155. Min Stack
# minHeap solution
import heapq
class MinStack(object):
    def __init__(self):
        self.stack = []
        self.minHeap = []
        heapq.heapify(self.minHeap)

    def push(self, x):
        self.stack.append(x)
        heapq.heappush(self.minHeap, x)

    def pop(self):
        item = self.stack.pop()
        self.minHeap = self.stack[:]
        heapq.heapify(self.minHeap)
        return item

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minHeap[0]

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
print(minStack.pop())
print(minStack.getMin())

