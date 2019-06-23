# 1013. Partition Array Into Three Parts With Equal Sum
class Solution:
    def canThreePartsEqualSum(self, A) -> bool:
        arr = [A[0]]
        for i in range(1, len(A)):
            arr.append(arr[i-1] + A[i])
            
        if arr and arr[-1] % 3 == 0:
            cur = step = arr[-1] // 3
            
            for x in arr:
                if cur == arr[-1]:
                    return True
                
                if cur == x:
                    cur += step
                    
        return False

print(Solution().canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))
            