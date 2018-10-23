# select min or max element and put it to proper spot
def selectionSort(nums):
    l = len(nums)
    for i in range(l):
        minIndex = i
        # find minimum number
        for j in range(i + 1, l):
            minIndex = (minIndex, j)[nums[minIndex] > nums[j]]
        # swap
        nums[i], nums[minIndex] = nums[minIndex], nums[i]

    return nums

print(selectionSort([2,2,3,34,5,6,64]))