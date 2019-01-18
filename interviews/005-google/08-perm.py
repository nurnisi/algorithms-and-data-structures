"""
You are given a string input that consists of 
uppercase ascii letters, 'A' to 'Z'. Write a 
function that returns the first index i, such 
that input[i]...input[i+25] forms a permutation 
of all letters 'A', 'Z'.
"""

def permutation(S):
    arr, i = [0]*26, 0
    while i < len(S):
        arr[ord(S[i]) - ord('A')] += 1
        if i >= 26: arr[ord(S[i-26]) - ord('A')] -= 1
        if ''.join(map(str, arr)) == "11111111111111111111111111":
            return i - 25
        i += 1
    return -1

print(permutation("ABFAABCBCDEFGHIJKLMNOPQRSTUVWXYZAHFJF"))
print(len("11111111111111111111111111"))
print(len("BCDEFGHIJKLMNOPQRSTUVWXYZA"))

