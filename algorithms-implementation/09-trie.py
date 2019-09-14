def make_trie(*words):
    root = dict()
    for w in words:
        cur = root
        for ch in w:
            cur = cur.setdefault(ch, {})
        cur['end'] = 'end'
    
    return root

def in_trie(trie, word):
    cur = trie
    for ch in word:
        if ch in cur:
            cur = cur[ch]
        else:
            return False
    return 'end' in cur

trie = make_trie(*['asd', 'fgh', 'jhk'])
print(in_trie(trie, 'asf'))

