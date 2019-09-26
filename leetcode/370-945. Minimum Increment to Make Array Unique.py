# 945. Minimum Increment to Make Array Unique
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A_srt = sorted(A) + [float('inf')]
        dups = []
        n, i, moves = len(A_srt), 0, 0
        while i < n-1:
            if A_srt[i] == A_srt[i+1]:
                dups.append(A_srt[i+1])
            else:
                cur = A_srt[i]+1
                while cur < A_srt[i+1] and dups:
                    moves += cur - dups.pop()
                    cur += 1
            i += 1
        return moves