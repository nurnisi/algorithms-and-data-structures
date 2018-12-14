# 46. Permutations
from collections import deque
class Solution:
    # my recursive solution
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        queue, ans = deque(nums), []
        self.helper(queue, [], len(nums), ans)
        return ans
    
    def helper(self, queue, perm, n, ans):
        if len(perm) == n:
            ans.append(perm.copy())
        m = len(queue)
        for i in range(m):
            perm.append(queue.popleft())
            self.helper(queue, perm, n, ans)
            queue.append(perm.pop())

    # shorter solution with ranges
    def permute2(self, nums):
        ans, n = [], len(nums)
        self.helper2(nums, 0, ans, n)
        return ans

    # permute num[begin..end]
    # invariant: num[0..begin-1] have been fixed/permuted
    def helper2(self, nums, begin, ans, n):
        if begin >= n:
            ans.append(nums.copy())
        else:
            for i in range(begin, n):
                nums[begin], nums[i] = nums[i], nums[begin]
                self.helper2(nums, begin+1, ans, n)
                nums[begin], nums[i] = nums[i], nums[begin]
    
    # iterative
    def permute3(self, nums):
        perms = [[]]
        for n in nums:
            newPerms = []
            for p in perms:
                for i in range(len(p)+1):
                    newPerms.append(p[:i] + [n] + p[i:])
            perms = newPerms
        return perms
    
sol = Solution()
print(sol.permute3([1,2,3]))