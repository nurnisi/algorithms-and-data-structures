import heapq

class RGBStream:
    def __init__(self):
        self.maxheap_red = []
        self.maxheap_green = []
        self.maxheap_blue = []
        self.minheap_red = []
        self.minheap_green = []
        self.minheap_blue = []
        self.medians = [0, 0, 0]
        self.count = 0
        
    def setRGB(self, r, g, b):
        self.add(self.maxheap_red, self.minheap_red, r)
        self.add(self.maxheap_green, self.minheap_green, g)
        self.add(self.maxheap_blue, self.minheap_blue, b)
        self.count += 1
        rgb = [r, g, b]
        for i in range(3):
            self.medians[i] += rgb[i]

        print(self.showMedian())
        # print(self.showMean())

    def add(self, maxheap, minheap, color):
        heapq.heappush(maxheap, -color)
        
        if len(minheap) + 1 <= len(maxheap):
            heapq.heappush(minheap, -heapq.heappop(maxheap))
        if len(minheap) > len(maxheap):
            heapq.heappush(maxheap, -heapq.heappop(minheap))
    
    def showMedian(self):
        if self.count % 2 == 0:
            rm = (-self.maxheap_red[0] + self.minheap_red[0]) / 2
            gm = (-self.maxheap_green[0] + self.minheap_green[0]) / 2
            bm = (-self.maxheap_blue[0] + self.minheap_blue[0]) / 2
            return [rm, gm, bm]
        
        return [-self.maxheap_red[0], -self.maxheap_green[0], -self.maxheap_blue[0]]

    def showMean(self):
        return [m/self.count for m in self.medians]

rgbs = RGBStream()
rgbs.setRGB(2,2,2)
rgbs.setRGB(4,4,4)
rgbs.setRGB(5,5,5)
rgbs.setRGB(6,6,6)
rgbs.setRGB(3,3,3)
rgbs.setRGB(1,1,1)
rgbs.setRGB(0,0,0)

    
    