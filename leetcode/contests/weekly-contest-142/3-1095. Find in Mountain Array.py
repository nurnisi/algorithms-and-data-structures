# 1095. Find in Mountain Array
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray2(self, target: int, mountain_arr) -> int:
        l, r = 0, len(mountain_arr)
        while l < r:
            mid = (l + r) // 2
            if mid < len(mountain_arr) - 1 and mountain_arr[mid] < mountain_arr[mid + 1]:
                l = mid + 1
            else:
                r = mid
        
        ll, rr = 0, l
        while ll < rr:
            mid = (ll + rr) // 2
            if target == mountain_arr[mid]: return mid
            elif target < mountain_arr[mid]: rr = mid 
            else: ll = mid + 1

        ll, rr = l, len(mountain_arr)
        while ll < rr:
            mid = (ll + rr) // 2
            if target == mountain_arr[mid]: return mid
            elif target > mountain_arr[mid]: rr = mid - 1 
            else: ll = mid + 1

        return -1

    def findInMountainArray(self, target: int, mountain_arr) -> int:
        l, r = 0, mountain_arr.length()
        while l < r:
            mid = (l + r) // 2
            if mid < mountain_arr.length() - 1 and mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        
        ll, rr = 0, l
        while ll < rr:
            mid = (ll + rr) // 2
            if target == mountain_arr.get(mid): return mid
            elif target < mountain_arr.get(mid): rr = mid 
            else: ll = mid + 1

        ll, rr = l, mountain_arr.length()
        while ll < rr:
            mid = (ll + rr) // 2
            if target == mountain_arr.get(mid): return mid
            elif target > mountain_arr.get(mid): rr = mid - 1 
            else: ll = mid + 1

        return -1

print(Solution().findInMountainArray2(5, [1,5,2]))