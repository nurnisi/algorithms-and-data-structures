# 916. Word Subsets
import collections
class Solution:
    def wordSubsets(self, A, B):
        CA = [collections.Counter(a) for a in A]
        for i in range(len(A)): CA[i]["word"] = A[i]
        
        CB = collections.Counter(B[0])
        for b in B: CB &= collections.Counter(b)
            
        return [w["word"] for w in list(filter(lambda a: all(a.get(k, 0) >= v for k, v in CB.items()), CA))]

print(Solution().wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]))