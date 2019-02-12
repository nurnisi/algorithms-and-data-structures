# 384. Shuffle an Array
import random
class Solution2:

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

class Solution:

    def __init__(self, nums: 'List[int]'):
        self.nums = nums
        self.original = list(nums)

    def reset(self) -> 'List[int]':
        self.nums = self.original
        self.original = list(self.original)
        return self.nums

    def shuffle(self) -> 'List[int]':
        aux = list(self.nums)
        for i in range(len(self.nums)):
            ri = random.randrange(len(aux))
            self.nums[i] = aux.pop(ri)
        
        return self.nums

# Your Solution object will be instantiated and called as such:
obj = Solution([1,2,3])
print(obj.reset())
print(obj.shuffle())
print(obj.reset())
print(obj.shuffle())
print(obj.reset())
print(obj.shuffle())