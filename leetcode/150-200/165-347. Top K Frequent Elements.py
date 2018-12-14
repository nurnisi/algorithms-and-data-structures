# 347. Top K Frequent Elements
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

sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))
