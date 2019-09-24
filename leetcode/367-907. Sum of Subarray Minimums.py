# 907. Sum of Subarray Minimums
class Solution:
    # brute force: TLE
    def sumSubarrayMins2(self, A) -> int:
        n = len(A)
        ans = 0
        for i in range(n):
            for j in range(i+1, n+1):
                ans += min(A[i:j])
        
        return ans % (10**9 + 7)

    # brute force optimized: TLE
    def sumSubarrayMins3(self, A) -> int:
        n = len(A)
        ans = 0
        for i in range(n):
            cur_min = A[i]
            for j in range(i, n):
                if cur_min > A[j]:
                    cur_min = A[j]
                ans += cur_min
        
        return ans % (10**9 + 7)

    # monotonous stack
    def sumSubarrayMins4(self, A) -> int:
        # PLE: previous less element
        n = len(A)
        mon_stack, prev_less = [], [i for i in range(1,n+1)]
        for i in range(n):
            while mon_stack and A[mon_stack[-1]] > A[i]:
                mon_stack.pop()
            prev_less[i] = i - mon_stack[-1] if mon_stack else i+1
            mon_stack.append(i)

        # NLE: next less element
        mon_stack, next_less = [], [i for i in range(n, 0, -1)]
        for i in range(n):
            while mon_stack and A[mon_stack[-1]] > A[i]:
                j = mon_stack.pop()
                next_less[j] = i - j
            mon_stack.append(i)

        ans = 0
        for i in range(n):
            ans += A[i] * prev_less[i] * next_less[i]
        return ans % (10**9+7)

    # monotonous stack
    def sumSubarrayMins(self, A):
        n, mod = len(A), 10**9 + 7
        left, right, s1, s2 = [0] * n, [0] * n, [], []
        for i in range(n):
            count = 1
            while s1 and s1[-1][0] > A[i]: count += s1.pop()[1]
            left[i] = count
            s1.append([A[i], count])
        for i in range(n)[::-1]:
            count = 1
            while s2 and s2[-1][0] >= A[i]: count += s2.pop()[1]
            right[i] = count
            s2.append([A[i], count])
        return sum(a * l * r for a, l, r in zip(A, left, right)) % mod

A = [3,1,2,4]
print(Solution().sumSubarrayMins(A))
            
