# 384. Shuffle an Array
import random
class Solution:

    def __init__(self, nums: 'List[int]'):
        self.nums = nums
        self.n = len(nums)
        self.shuf = None

    def reset(self) -> 'List[int]':
        self.shuf = None
        return self.nums

    def shuffle(self) -> 'List[int]':
        if not self.shuf:
            self.shuf = [float('inf')] * self.n
            for num in self.nums:
                i = random.randint(0, self.n-1)
                while self.shuf[i] != float('inf'):
                    i = random.randint(0, self.n-1)
                self.shuf[i] = num
        return self.shuf

# Your Solution object will be instantiated and called as such:
obj = Solution([1,2,3])
print(obj.reset())
print(obj.shuffle())