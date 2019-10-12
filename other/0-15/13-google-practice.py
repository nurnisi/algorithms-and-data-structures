def make_trie(S):
    trie = {}
    for s in S:
        cur = trie
        for ch in s:
            cur = cur.setdefault(ch, {})
        cur['end'] = 'end'
    return trie

def max_dist(S):
    ans = 0
    trie = {}

    for s in S:
        cur = trie
        n = len(s)
        for i, ch in enumerate(s):
            if ch not in cur:
                opp = 'max' + str(int(ch)^1)
                if opp in cur:
                    ans = max(ans, cur[opp] + n - i)    
                cur[ch] = {}
                cur['max' + ch] = n - i
                cur = cur[ch]
            else:
                cur['max' + ch] = max(cur['max' + ch], n - i)
                cur = cur[ch]

    return ans

S = ['1011000000', '10111101']
print(max_dist(S))
