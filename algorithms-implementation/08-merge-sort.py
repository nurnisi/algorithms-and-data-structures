def mergeSort(nums):
    helper(nums, 0, len(nums) - 1)
    return nums

def helper(nums, l, r):
    if l < r:
        m = int((l + r) / 2) # find the middle
        helper(nums, l, m) # mergeSort on the left
        helper(nums, m + 1, r) # mergeSort on the right
        merge(nums, l, m, r) # merge to sides

def merge(nums, l, m, r):
    # copy elements to  temp arrays
    l1, l2 = m - l + 1, r - m # determine length of arrays
    L, R = [0] * l1, [0] * l2 # create temp arrays
    for i in range(l1): L[i] = nums[l + i]
    for i in range(l2): R[i] = nums[m + i + 1]

    #merge
    i, j, k = 0, 0, l # starting indexes
    while i < l1 and j < l2:
        if L[i] < R[j]:
            nums[k] = L[i]
            i += 1
        else:
            nums[k] = R[j]
            j += 1
        k += 1

    # leftovers
    while i < l1:
        nums[k] = L[i]
        k += 1
        i += 1
    while j < l2:
        nums[k] = R[j]
        k += 1
        j += 1

print(mergeSort([76,3,100,6,12,2,5,34]))