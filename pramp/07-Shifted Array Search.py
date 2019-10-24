# [9, 12, 2, 4, 5]

# [9, 12, 17, 18, 2, 4]

def shifted_arr_search(shiftArr, num):
  n = len(shiftArr)
  
  def binaryPivot(shiftArr):
    l, r = 0, n-1
    while l < r:
      m = (l + r) // 2
      if shiftArr[m] > shiftArr[m+1]:
        return m
      elif shiftArr[r] < shiftArr[m]:
        l = m + 1
      else:
        r = m
    
    return -1
    
  def binarySearch(arr, l, r, num):
    while l <= r:
      m = (l + r) // 2
      print(l, r, m)
      if arr[m] == num:
        return m
      if arr[m] > num:
        r = m - 1
      else:
        l = m + 1
    
    return -1
    
  pivot = binaryPivot(shiftArr)
  # print(pivot)
  if pivot == -1:
    return binarySearch(shiftArr, 0, n-1, num)
  else:
    if shiftArr[0] <= num and shiftArr[pivot] >= num:
      return binarySearch(shiftArr, 0, pivot, num)
    else:
      return binarySearch(shiftArr, pivot+1, n-1, num)

print(shifted_arr_search([2], 2))
print(shifted_arr_search([9, 12, 17, 18, 2, 4], 2))
        
    