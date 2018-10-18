# 53. Maximum Subarray
# attempt 1: does not work
def maxSubArray2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0: return 0
        
    sums = []
    sums.append(nums[0])
    mini = maxi = 0
    for i in range(1, len(nums)):
        sums.append(sums[-1] + nums[i])
        mini = i if sums[mini] > sums[-1] else mini
        maxi = i if sums[maxi] < sums[-1] else maxi
    
    return max(nums[mini], nums[maxi]) if maxi <= mini else sums[maxi] - sums[mini]

def maxSubArray(nums):
    mini = maxi = curSum = nums[0]
    for i in range(0, len(nums)):
        curSum += nums[i]
        maxi = max(maxi, nums[i], curSum - mini)
        mini = min(curSum, mini)

    return maxi


def maxSubArray3(self, nums):
    dp = []
    dp.append(nums[0])
    maxi = nums[0]
    for i in range(1, len(nums)):
        dp.append(nums[i] + (dp[i-1] if dp[i-1] > 0 else 0))
        maxi = max(maxi, dp[i])
    return maxi




print(maxSubArray([8]))
print(maxSubArray([-2,-1]))
print(maxSubArray([-1,-2]))
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([-1,0]))
print(maxSubArray([1,2]))
print(maxSubArray([-1]))