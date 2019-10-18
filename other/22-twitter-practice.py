import heapq

class RGBStream:
    def __init__(self):
        self.maxheap_red = []
        self.maxheap_green = []
        self.maxheap_blue = []
        self.minheap_red = []
        self.minheap_green = []
        self.minheap_blue = []
        
    def setRGB(self, r, g, b):
        self.add(self.maxheap_red, self.)

    def add(self, maxheap, minheap, color):
        heapq.heappush(maxheap, color)
        
        if minheap and maxheap[0] > minheap[0]:
            heapq.heappush(minheap, heapq.heappop(maxheap))
        if len(minheap) > len(maxheap):
            heapq.heappush(maxheap, heapq.heappop(minheap))
    