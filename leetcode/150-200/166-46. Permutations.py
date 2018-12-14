# 46. Permutations
from collections import deque
class Solution:
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
    
sol = Solution()
print(sol.permute([1,2,3]))