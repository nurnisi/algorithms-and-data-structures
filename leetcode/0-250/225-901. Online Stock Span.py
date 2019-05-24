# 901. Online Stock Span
# brute force: TLE
class StockSpanner2:

    def __init__(self):
        self.arr = []

    def next(self, price):
        self.arr.append(price)
        i = len(self.arr) - 1
        while i >= 0 and self.arr[i] <= price:
            i -= 1
        if i < 0: return len(self.arr)
        return len(self.arr) - i - 1

# stack
class StockSpanner3:

    def __init__(self):
        self.cur = 0
        self.stack = []

    def next(self, price):
        self.cur += 1
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        ans = self.cur - self.stack[-1][1] if self.stack else self.cur
        self.stack.append((price, self.cur))
        return ans

# stack: leetcode
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price):
        weight = 1
        while self.stack and self.stack[-1][0] <= price:
            weight += self.stack.pop()[1]
        self.stack.append((price, weight))
        return weight

# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
print(obj.next(100))
print(obj.next(80))
print(obj.next(60))
print(obj.next(70))
print(obj.next(60))
print(obj.next(75))
print(obj.next(85))