# 1128. Number of Equivalent Domino Pairs
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        arr = [0] * 100
        for a, b in dominoes:
            if (a > b):
                a, b = b, a
            arr[a * 10 + b] += 1
        
        cnt = 0
        for x in arr:
            for y in range(x):
                cnt += y
                
        return cnt