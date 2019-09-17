# Array Index & Element Equality
def index_equals_value_search(arr):
    l, r = 0, len(arr)
    while l < r:
        mid = (l+r)//2
        if arr[mid] < mid:
            l = mid+1
        else:
            r = mid
  
    if arr[l] == l:
        return l
  
    return -1