# 96. Unique Binary Search Trees
class Solution:
    def numTrees2(self, n):
        d = {0: 1, 1: 1}
        def helper(left, right):
            ans = 0
            for i in range(left, right+1):
                if i-left not in d: 
                    d[i-left] = helper(left, i-1)
                if right-i not in d: 
                    d[right-i] = helper(i+1, right)
                ans += (d[i-left] * d[right-i])   
            return ans
        ans = helper(1, n)
        return ans

    def numTrees3(self, n):
        G = [0] * (n+1)
        G[0] = G[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]
        return G[n]

    def numTrees(self, n):
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)
                    
sol = Solution()
print(sol.numTrees(1))
print(sol.numTrees(2))
print(sol.numTrees(3))
print(sol.numTrees(4))
print(sol.numTrees(5))
print(sol.numTrees(6))
print(sol.numTrees(7))
                


        