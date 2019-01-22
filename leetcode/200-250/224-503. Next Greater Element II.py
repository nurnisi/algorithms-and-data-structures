# 503. Next Greater Element II
class Solution:
    # brute force: n^2
    def nextGreaterElements2(self, nums):
        n = len(nums)
        ans = [-1] * n
        for i in range(n):
            j = (i + 1) % n
            while j != i:
                if nums[i] < nums[j]:
                    ans[i] = nums[j]
                    break
                j = (j + 1) % n
        
        return ans

    # stack
    def nextGreaterElements(self, nums):
        n = len(nums)
        stack, ans = [], [-1]*n
        for i in range(n*2-1,-1,-1):
            j = i % n
            while stack:
                if stack[-1] <= nums[j]: stack.pop()
                else: break
            if stack: ans[j] = stack[-1]
            stack.append(nums[j])
            i -= 1
        return ans

sol = Solution()
print(sol.nextGreaterElements([1,2,1]))
        