def insertionSort(nums):
    for i in range(1, len(nums)):
        j = i
        # swap an element until it is not smaller that its predecessors
        while j > 0 and nums[j] < nums[j-1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
    return nums

print(insertionSort([7,4,3]))
        