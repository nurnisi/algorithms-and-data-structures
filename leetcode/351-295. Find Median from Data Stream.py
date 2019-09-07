# 295. Find Median from Data Stream
class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        l, r = 0, len(self.arr)
        while l < r:
            m = (l+r)//2
            if self.arr[m] > num:
                r = m
            else:
                l = m+1
        self.arr.insert(l, num)

    def findMedian(self) -> float:
        n = len(self.arr)
        if n%2 == 0:
            return (self.arr[n//2-1] + self.arr[n//2]) / 2
        return self.arr[n//2]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()