# 692. Top K Frequent Words
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = collections.Counter(words)
        
        d = collections.defaultdict(list)
        for key, val in cnt.items():
            d[val].append(key)
        
        ans = []
        for i in sorted(d.keys(), reverse=True):
            ans += sorted(d[i])[:min(len(d[i]), k)]
            k -= len(d[i])
            if k < 0:
                break
        
        return ans

class Element:
    
    def __init__(self, word, count):
        self.word = word
        self.count = count
        
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count
    
    def __eq__(self, other):
        return self.count == other.count and self.word == other.word

class Solution:
    
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = collections.Counter(words)
        
        h = []
        heapq.heapify(h)
        for word, count in counts.items():
            heapq.heappush(h, Element(word, count))
            if len(h) > k:
                heapq.heappop(h)
        
        ans = []
        while h:
            ans.append(heapq.heappop(h).word)
        return ans[::-1]
        