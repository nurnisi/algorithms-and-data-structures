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
        l, r = 1, len(mountain_arr) - 2
        while l < r:
            mid = (l + r) // 2
            a, b, c = mountain_arr[mid - 1], mountain_arr[mid], mountain_arr[mid + 1]
            if a < b > c: 
                l = mid
                break
            if a < b < c: l = mid + 1
            else: r = mid - 1

        if mountain_arr[l] == target: return l

        ll, rr = 0, l
        while ll < rr:
            mid = (ll + rr) // 2
            if target == mountain_arr[mid]: return mid
            elif target < mountain_arr[mid]: rr = mid - 1 
            else: ll = mid + 1
        
        if mountain_arr[ll] == target: return ll

        ll, rr = l, len(mountain_arr) - 1
        while ll < rr:
            mid = (ll + rr) // 2
            if target == mountain_arr[mid]: return mid
            elif target > mountain_arr[mid]: rr = mid - 1 
            else: ll = mid + 1

        if mountain_arr[ll] == target: return ll
        return -1

    def findInMountainArray(self, target: int, mountain_arr) -> int:
        n = mountain_arr.length()
        l, r = 1, n - 2
        while l < r:
            mid = (l + r) // 2
            a, b, c = mountain_arr.get(mid - 1), mountain_arr.get(mid), mountain_arr.get(mid + 1)
            if a < b > c: 
                l = mid
                break
            if a < b < c: l = mid + 1
            else: r = mid - 1

        if mountain_arr.get(l) == target: return l

        ll, rr = 0, l
        while ll < rr:
            mid = (ll + rr) // 2
            a = mountain_arr.get(mid)
            if target == a: return mid
            elif target < a: rr = mid - 1 
            else: ll = mid + 1

        if mountain_arr.get(ll) == target: return ll

        ll, rr = l, n - 1
        while ll < rr:
            mid = (ll + rr) // 2
            a = mountain_arr.get(mid)
            if target == a: return mid
            elif target > a: rr = mid - 1 
            else: ll = mid + 1

        if mountain_arr.get(ll) == target: return ll
        return -1

# print(Solution().findInMountainArray2(5, [1,5,2]))
# print(Solution().findInMountainArray2(3, [1,2,3,4,5,3,1]))
# print(Solution().findInMountainArray2(3, [0,1,2,4,2,1]))
# print(Solution().findInMountainArray2(0, [1,2,3,5,3]))
# print(Solution().findInMountainArray2(2, [1,2,3,4,5,3,1]))
print(Solution().findInMountainArray2(101, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82]))
