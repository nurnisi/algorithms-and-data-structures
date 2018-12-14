# 347. Top K Frequent Elements
import collections
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1

        d = sorted(d.items(), key=lambda item: item[1], reverse=True)
        ans = []
        for i in range(k):
            ans.append(d[i][0])
        
        return ans
    
    def topKFrequent2(self, nums, k):
        count = collections.Counter(nums)
        return sorted(count.items(), key=lambda item: item[1], reverse=True)[:k]

    def topKFrequent3(self, nums, k):
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)

sol = Solution()
print(sol.topKFrequent3([1,1,1,2,2,3], 2))
