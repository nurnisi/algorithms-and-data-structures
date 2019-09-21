# String A, B
A = "abcd aabc bd"
B = "aaa aa"

import collections
def count(Arr):
    Arr = Arr.split()
    A_freq = [[0]*26 for _ in Arr]
    A_sml = []
    for i, s in enumerate(Arr):
        for ch in s:
            A_freq[i][ord(ch) - ord('a')] += 1
        for cnt in A_freq[i]:
            if cnt > 0:
                A_sml.append(cnt)
                break
    return A_sml

def func(A, B):
    AA = count(A)
    BB = count(B)

    ans = []
    for b in BB:
        cnt = 0
        for a in AA:
            cnt += 1 if a < b else 0
        ans.append(cnt)    

    return ans 

print(func(A, B))

