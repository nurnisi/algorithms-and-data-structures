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