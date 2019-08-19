# 665. Non-decreasing Array
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt = 0
        flag = True
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                cnt += 1
                if cnt > 1: return False
                else:
                    flag = i == 0 or nums[i-1] <= nums[i+1] \
                        or i == len(nums)-2 or nums[i] <= nums[i+2]
        
        return flag