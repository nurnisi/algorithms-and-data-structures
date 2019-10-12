import collections
def shortestPrefix(words):
    ans = []
    wordsCopy = words[:]
    i = 1
    while len(ans) < len(words):
        d = collections.defaultdict(list)
        for w in wordsCopy:
            d[w[:i]].append(w)
        
        tempWords = []
        for pref, wordList in d.items():
            if len(wordList) == 1:
                ans.append(pref)
            else:
                tempWords.extend(wordList)
        wordsCopy = tempWords[:]

        i += 1

    return ans

print(shortestPrefix(['apple', 'toy', 'angel', 'angular', 'tofu']))

# n = len(words)
# k = length of the longest word
# time: O(n*k)
# space: O(n)