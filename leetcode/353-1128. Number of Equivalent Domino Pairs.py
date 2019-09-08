# 1128. Number of Equivalent Domino Pairs
import collections
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dictio = collections.defaultdict(int)
        pairs = 0
        for d in dominoes:
            dh = min(d)*10 + max(d)
            pairs += dictio[dh]
            dictio[dh] += 1
        
        return pairs