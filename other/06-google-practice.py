# String A, B
A = "abcd aabc bd"
B = "aaa aa"

# my solution
import collections
def count2(Arr):
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
def func3(A, B):
    A, B = A.split(), B.split()
    ans = []
    for b in B:
        cnt = 0
        for a in A:
            if b.count(min(b)) > a.count(min(a)):
                cnt += 1
        ans.append(cnt)
    return ans

# leetcode solution 2
def count(a):
    a, af, am = a.split(), [[0]*26 for _ in a], []
    for i, s in enumerate(a):
        for ch in s:
            af[i][ord(ch) - ord('a')] += 1
        for cnt in af[i]:
            if cnt > 0:
                am.append(cnt)
                break
    return am

def func(A, B):
    A, B = count(A), count(B)
    sm = [0]*11
    for cnt in A:
        sm[cnt] += 1
    csm = [0]
    for s in sm[1:]:
        csm.append(csm[-1] + s)
    
    ans = []
    for b in B:
        ans.append(csm[b-1])

    return ans

print(func(A, B))

