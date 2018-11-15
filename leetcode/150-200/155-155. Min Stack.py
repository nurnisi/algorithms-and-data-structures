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

# one stack solution
class MinStack2(object):
    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, x):
        # only push the old minimum value when the current 
        # minimum value changes after pushing the new value x
        if self.min == None or x <= self.min:
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)

    def pop(self):
        # if pop operation could result in the changing of the current minimum value, 
        # pop twice and change the current minimum value to the last minimum value.
        if self.stack.pop() == self.min: self.min = self.stack.pop()
    
    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min

minStack = MinStack2()
minStack.push(0)
minStack.push(1)
minStack.push(0)
print(minStack.getMin())
minStack.pop()
print(minStack.getMin())

