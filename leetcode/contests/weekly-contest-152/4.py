class Solution:
    # TLE
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        set_words = [set(w) for w in words]
        set_puzzs = [set(p) for p in puzzles]
        
        ans = []
        for i, p in enumerate(set_puzzs):
            cnt = 0
            for w in set_words:
                if puzzles[i][0] in w and all(c in p for c in w):
                    cnt += 1
            ans.append(cnt)
        
        return ans