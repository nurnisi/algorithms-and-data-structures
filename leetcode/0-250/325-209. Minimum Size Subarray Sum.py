# 209. Minimum Size Subarray Sum
class Solution:
    def minSubArrayLen2(self, s: int, nums) -> int:
        i = j = 0
        ans, cur_sum = float('inf'), 0
        
        while j < len(nums) or cur_sum >= s:
            if i == j or cur_sum < s:
                cur_sum += nums[j]
                j += 1
            else:
                ans = min(ans, j-i)
                cur_sum -= nums[i]
                i += 1
        
        return ans if ans != float('inf') else 0

    def minSubArrayLen(self, s: int, nums) -> int:
        cum = [0]
        for x in nums:
            cum.append(cum[-1] + x)
        
        ans = float('inf')
        n = len(cum)
        for i in range(n):
            l, r = i, n
            while l < r:
                mid = (l+r)//2
                if cum[mid] - cum[i] >= s:
                    r = mid
                else:
                    l = mid+1
            if l < n and cum[l] - cum[i] >= s:
                ans = min(ans, l-i)
            
        return ans if ans != float('inf') else 0

print(Solution().minSubArrayLen(7, [2,3,1,2,4,3]))
print(Solution().minSubArrayLen(11, [1,2,3,4,5]))