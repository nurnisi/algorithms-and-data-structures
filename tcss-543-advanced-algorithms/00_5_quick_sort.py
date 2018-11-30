def quickSort(nums):
    helper(nums, 0, len(nums) - 1)
    return nums

def helper(nums, l, r):
    if l < r:
        # partition
        p = partition(nums, l, r)
        # recurse to left and right
        helper(nums, l, p - 1)
        helper(nums, p + 1, r)

def partition(nums, l, r):
    # put elements that are less than pivot to the left
    # and that are bigger than pivot to the right
    i = l - 1
    for j in range(l, r):
        if nums[j] <= nums[r]: # the last element num[r] is chosen as pivot
            i += 1
            nums[i], nums[j] = nums[j], nums[i] 
            
    # swap pivot to its spot
    nums[i + 1], nums[r] = nums[r], nums[i + 1]
    return i + 1

print(quickSort([5,53,2,34,8,1,73,5]))