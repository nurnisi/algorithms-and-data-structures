def pattern_matching(str1, str2):
    n, m = len(str1), len(str2)
    if n > m:
        return False

    comp1 = compress(str1, n)
    comp2 = compress(str2, m)

    d = {"0": "A", "1": "B"}

    return all(d[comp1[-i]] == comp2[-i] for i in range(1, len(comp2)+1))

def compress(str, n):
    compressed = []
    prev, i = str[0], 0
    while i < n:
        while i < n and prev == str[i]:
            i += 1
        compressed.append(prev)
        if i < n:
            prev = str[i]
    
    return compressed

print(pattern_matching("0100", "AABBBAAA"))
print(pattern_matching("01011", "AAAABBBB"))

