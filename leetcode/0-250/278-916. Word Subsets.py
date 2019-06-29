# 916. Word Subsets
import collections
class Solution:
    def wordSubsets2(self, A, B):
        CA = [collections.Counter(a) for a in A]
        for i in range(len(A)): CA[i]["word"] = A[i]
        
        CB = collections.Counter(B[0])
        for b in B: CB &= collections.Counter(b)
            
        return [w["word"] for w in list(filter(lambda a: all(a.get(k, 0) >= v for k, v in CB.items()), CA))]

    def wordSubsets(self, A, B):
        def count(w):
            ans = [0] * 26
            for c in w:
                ans[ord(c) - ord('a')] += 1
            return ans
        
        bmax = [0] * 26
        for b in B:
            for i, c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)
        
        ans = []
        for a in A:
            if all(x >= y for x, y in zip(count(a), bmax)):
                ans.append(a)
        return ans

print(Solution().wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]))