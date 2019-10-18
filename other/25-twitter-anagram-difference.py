import collections
def anagram_difference(A, B):
    ans = []
    for i in range(len(A)):
        if len(A[i]) != len(B[i]):
            ans.append(-1)
            continue

        da = collections.Counter(A[i])
        db = collections.Counter(B[i])

        seta = set()
        for ch, cnt in da.items():
            for i in range(cnt):
                seta.add(ch + str(i))
        
        setb = set()
        for ch, cnt in db.items():
            for i in range(cnt):
                setb.add(ch + str(i))
        
        setuni = seta & setb
        ans.append((len(seta) + len(setb) - 2 * len(setuni)) // 2)

    return ans

print(anagram_difference(['a', 'jk', 'abb', 'mn', 'abc'], ['bb', 'kj', 'bbc', 'op', 'def']))
