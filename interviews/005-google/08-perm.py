"""
You are given a string input that consists of 
uppercase ascii letters, 'A' to 'Z'. Write a 
function that returns the first index i, such 
that input[i]...input[i+25] forms a permutation 
of all letters 'A', 'Z'.
"""

def permutation2(S):
    arr, i = [0]*26, 0
    while i < len(S):
        arr[ord(S[i]) - ord('A')] += 1
        if i >= 26: arr[ord(S[i-26]) - ord('A')] -= 1
        if ''.join(map(str, arr)) == ''.join(['1']*26):
            return i - 25
        i += 1
    return -1

def permutation(S):
    arr, i, count = [0]*26, 0, 0
    while i < len(S):
        c1 = ord(S[i]) - ord('A')
        if not arr[c1]: count += 1
        arr[c1] += 1
        if i >= 26:
            c2 = ord(S[i-26]) - ord('A')
            arr[c2] -= 1
            if not arr[c2]: count -= 1
        if count == 26:
            return i - 25
        i += 1
    return -1

print(permutation("BBCDEFGHIJKLMNOPQRSTUVWXYZAHFJF"))

