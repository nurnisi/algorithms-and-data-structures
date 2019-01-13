# 703. Kth Largest Element in a Stream
class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        self.nums.sort(reverse=True)

    def add(self, val):
        l, r = 0, len(self.nums)
        while l < r:
            mid = (l + r) // 2
            if self.nums[mid] > val: l = mid + 1
            else: r = mid
        self.nums = self.nums[:l] + [val] + self.nums[l:]
        print(self.nums)
        return self.nums[self.k - 1]

sol = KthLargest(1, [-2])
print(sol.add(-3))
print(sol.add(0))
print(sol.add(2))
print(sol.add(-1))
print(sol.add(4))
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)