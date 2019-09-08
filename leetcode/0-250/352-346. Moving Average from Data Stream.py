# 346. Moving Average from Data Stream
import collections
class MovingAverage:

    def __init__(self, size: int):
        self.nums = collections.deque()
        self.cur_sum = 0
        self.size = size
        

    def next(self, val: int) -> float:
        if len(self.nums) == self.size:
            self.cur_sum -= self.nums.popleft()
        self.nums.append(val)
        self.cur_sum += val
        return self.cur_sum / len(self.nums)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)