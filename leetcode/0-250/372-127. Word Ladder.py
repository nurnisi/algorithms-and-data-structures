# 127. Word Ladder
import collections
class Solution:
    # TLE
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if endWord not in wordList:
            return 0
        
        self.ans = float('inf')
        self.n = len(wordList)
        
        # create a dictionary
        self.d = collections.defaultdict(list)
        for kw in set([beginWord] + wordList):
            for vw in wordList:
                if sum(c1 != c2 for c1, c2 in zip(kw, vw)) == 1:
                    self.d[kw].append(vw)        
        
        def dfs(depth, curWord, seen):
            if depth > self.n:
                return
            if curWord == endWord:
                self.ans = min(self.ans, depth)
                return
            
            for w in self.d[curWord]:
                if w not in seen:
                    seen.add(w)
                    dfs(depth+1, w, seen)
                    seen.remove(w)
        
        dfs(1, beginWord, set([beginWord]))
        return self.ans if self.ans != float('inf') else 0

    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        d = collections.defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                blanked = w[:i] + '_' + w[i+1:]
                d[blanked].append(w)
                
        q, seen = collections.deque([(beginWord, 1)]), set()
        while q:
            word, steps = q.popleft()
            if word not in seen:
                seen.add(word)
                if word == endWord:
                    return steps
                for i in range(len(word)):
                    blanked = word[:i] + '_' + word[i+1:]
                    q.extend((nw, steps+1) for nw in d[blanked])
        
        return 0
                
    
print(Solution().ladderLength("a", "c", ["a","b","c"]))
print(Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
print(Solution().ladderLength("hot", "dog", ["hot","dog","dot"]))
