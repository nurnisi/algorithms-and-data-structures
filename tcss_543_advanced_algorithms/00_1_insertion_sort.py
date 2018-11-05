# insert an element to to proper spot
def insertionSort(nums):
    for i in range(1, len(nums)):
        j = i
        cur = nums[i]
        # find a spot to insert an element at index j
        while j > 0 and cur < nums[j - 1]:
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = cur

    return nums

print(insertionSort([7,6,3,23,1,8,54]))
        