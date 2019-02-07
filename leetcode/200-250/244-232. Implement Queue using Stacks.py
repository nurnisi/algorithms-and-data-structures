# 232. Implement Queue using Stacks
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: 'int') -> 'None':
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)
        

    def pop(self) -> 'int':
        """
        Removes the element from in front of queue and returns that element.
        """
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())
            
        elem = self.stack1.pop()
        
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        
        return elem

    def peek(self) -> 'int':
        """
        Get the front element.
        """
        return self.stack1[0]
        

    def empty(self) -> 'bool':
        """
        Returns whether the queue is empty.
        """
        return not self.stack1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()