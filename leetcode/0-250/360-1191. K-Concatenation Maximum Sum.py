# 1191. K-Concatenation Maximum Sum
class Solution:
    def kConcatenationMaxSum(self, arr, k: int) -> int:
        dp = [arr[0]]
        for n in arr[1:]:
            dp.append(max(n, dp[-1]+n))
        mx = max(dp)
        
        rnd = 0
        if k > 1:
            dp_rnd = [arr[0]]
            for n in arr[1:]+arr:
                dp_rnd.append(max(n, dp_rnd[-1]+n))
            rnd = max(dp_rnd)
        
        sm = sum(arr)
        betw = 0
        if k > 2:
            betw = rnd + sm * (k-2)
        
        return max(mx, rnd, betw, sm*k, 0) % (10**9 + 7)