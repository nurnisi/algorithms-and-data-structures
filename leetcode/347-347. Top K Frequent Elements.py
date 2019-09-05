# 347. Top K Frequent Elements
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [key for key, val in sorted(collections.Counter(nums).items(), key=lambda kv: kv[1], reverse=True)][:k]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        counts = [set()]
        
        for x in nums:
            if x not in d:
                d[x] = 1
                counts[d[x]-1].add(x)
            else:
                counts[d[x]-1].discard(x)
                d[x] += 1
                if d[x]-1 >= len(counts):
                    counts.append(set())
                counts[d[x]-1].add(x)
        
        ans = []
        i = len(counts)-1
        while i >= 0 and len(ans) < k:
            ans.extend(counts[i])
            i -= 1
        
        return ans

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        buckets = [[] for _ in nums]
        for num, freq in counts.items():
            buckets[-freq].append(num)
        
        ans = []
        for b in buckets:
            ans.extend(b)
            if len(ans) == k: break
        return ans