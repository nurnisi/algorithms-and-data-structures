def find_duplicates_two_pointer(arr1, arr2):
  i = j = 0
  intersections = []
  
  while i < len(arr1) and j < len(arr2):
    if arr1[i] == arr2[j]:
      intersections.append(arr1[i])
      
    if arr1[i] < arr2[j]:
      i += 1
    else:
      j += 1
      
  return intersections

def find_duplicates(arr1, arr2):
  intersections = []
  if len(arr1) > len(arr2):
    # binary search on arr1
    for x in arr2:
      i = binary_search(arr1, x)
      if i != -1 and arr1[i] == x:
        intersections.append(x)
  else:
    # binary search on arr2
    for x in arr1:
      i = binary_search(arr2, x)
      if i != -1 and arr2[i] == x:
        intersections.append(x)
        
  return intersections

def binary_search(arr, x):
  l, r = 0, len(arr)-1
  while l <= r:
    m = (l + r) // 2
    if arr[m] == x:
      return m
    elif arr[m] < x:
      l = m + 1
    else:
      r = m - 1
  
  return -1