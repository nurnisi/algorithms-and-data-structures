# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, K):
    # write your code in Python 3.6
    i, j = len(S)-1, 0
    ans = []
    while i >= 0:
        if j == K:
            j = 0
            ans.append('-')
        if S[i] != '-':
            ans.append(S[i].upper())
            i -= 1
            j += 1
        else:
            i -= 1
    ans.reverse()
    return ''.join(ans)
            
print(solution("2-4A0r7-4k", 0))