# String A, B
A = "abcd aabc bd"
B = "aaa aa"

# my solution
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

def func2(A, B):
    AA = count(A)
    BB = count(B)

    ans = []
    for b in BB:
        cnt = 0
        for a in AA:
            cnt += 1 if a < b else 0
        ans.append(cnt)    

    return ans 

# leetcode solution
def func(A, B):
    A, B = A.split(), B.split()
    ans = []
    for b in B:
        cnt = 0
        for a in A:
            if b.count(min(b)) > a.count(min(a)):
                cnt += 1
        ans.append(cnt)
    return ans


print(func(A, B))

