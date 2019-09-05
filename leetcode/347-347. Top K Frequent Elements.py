# 347. Top K Frequent Elements
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [key for key, val in sorted(collections.Counter(nums).items(), key=lambda kv: kv[1], reverse=True)][:k]