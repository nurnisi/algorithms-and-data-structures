# at the end of each iteration puts next largest item to its spot(end)
def bubbleSort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    
    return nums

print(bubbleSort([4,3,3,67,3,2,2,7]))
