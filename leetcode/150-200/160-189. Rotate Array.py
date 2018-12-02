# 189. Rotate Array
class Solution:
    # with auxiliary array
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        if n == 1 or k == 0 or k == n: return
        temp = nums[-k:]
        for i in range(n-k-1, -1, -1):
            nums[i+k] = nums[i]
        
        nums[:k] = temp

    # without auxiliary array
    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        if n == 1 or k == 0 or k == n: return
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)

    def reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    # cyclic replacements
    def rotate3(self, nums, k):
        count, start, n = 0, 0, len(nums)
        k = k % n
        while count < n:
            cur = start
            prev = nums[cur]
            while True:
                nxt = (cur + k) % n
                temp = nums[nxt]
                nums[nxt] = prev
                prev = temp
                cur = nxt
                count += 1
                if cur == start:
                    break
            start += 1

sol = Solution()
nums = [1,2,3,4,5,6,7]
sol.rotate2(nums, 3)
print(nums)
nums = [1,2,3,4,5,6]
sol.rotate2(nums, 1)
print(nums)