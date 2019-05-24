# 232. Implement Queue using Stacks
class MyQueue:
    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: 'int') -> 'None':
        self.stack1.append(x)

    def pop(self) -> 'int':
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())
            
        elem = self.stack1.pop()
        
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        
        return elem

    def peek(self) -> 'int':
        return self.stack1[0]    

    def empty(self) -> 'bool':
        return not self.stack1
        
class MyQueue2:
    
    def __init__(self):
        self.front = None
        self.s1 = []
        self.s2 = []

    def push(self, x: 'int') -> 'None':
        if self.s2:
            while self.s2:
                self.s1.append(self.s2.pop())
        if not self.front: self.front = x
        self.s1.append(x)

    def pop(self) -> 'int':
        if self.s1:
            while self.s1:
                self.s2.append(self.s1.pop())
        elem = self.s2.pop()
        self.front = self.s2[-1] if self.s2 else None
        return elem

    def peek(self) -> 'int':
        return self.front

    def empty(self) -> 'bool':
        return not self.s1 and not self.s2

obj = MyQueue2()
obj.push(1)
obj.push(2)
print(obj.peek())
print(obj.pop())
print(obj.empty())