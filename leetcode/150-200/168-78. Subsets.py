# 78. Subsets
class Solution:
    # recursive
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans, stack, n = [[]], [], len(nums)
        def helper(cur):
            for i in range(cur, n):
                stack.append(nums[i])
                ans.append(stack.copy())
                helper(i + 1)
                stack.pop()
        helper(0)
        return ans

    # shorter recursive
    def subsets4(self, nums):
        ans, n = [], len(nums)
        def dfs(cur, subset):
            ans.append(subset)
            for i in range(cur, n):
                dfs(i+1, subset+[nums[i]])
        dfs(0, [])
        return ans

    # bit manipulation
    def subsets2(self, nums):
        n, ans = len(nums), []
        bit = 2**n

        for i in range(bit):
            subset, b = [], bin(i)[2:]
            lenb = len(b)
            for j in range(lenb):
                if int(b[j]):
                    subset.append(nums[n - lenb + j])
            ans.append(subset)

        return ans
    
    

    # iterative
    def subsets3(self, nums):
        print()

sol = Solution()
print(sol.subsets5([1,2,3]))
                