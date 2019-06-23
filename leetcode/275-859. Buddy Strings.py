# 859. Buddy Strings
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B) or len(A) == 1: return False
        
        # create array of indices, where A and B differ
        # also count character occurences
        dif, count = [], [0] * 26
        for i in range(len(A)):
            if A[i] != B[i]: dif.append(i)
            count[ord(A[i]) - ord('a')] += 1
        
        if len(dif) > 2: return False
        elif len(dif) == 2 and A[dif[0]] != B[dif[1]]: return False
        else: return any([c > 1 for c in count])

print(Solution().buddyStrings("abcaa", "abcbb"))