# 917. Reverse Only Letters
def reverseOnlyLetters(S):
    def isLetter(c):
        if (ord(c) >= 65 and ord(c) < 91) or (ord(c) >= 97 and ord(c) < 123):
            return True
        return False

    A = list(S)
    i, j = 0, len(A) - 1
    while i < j:
        if isLetter(A[i]) and isLetter(A[j]):
            A[i], A[j] = A[j], A[i]
            i = i + 1
            j = j - 1
        if not isLetter(A[i]):
            i = i + 1
        if not isLetter(A[j]):
            j = j - 1
    
    return ''.join(A)
            
print(reverseOnlyLetters("a-bC-dEf-ghIj"))

def reverseOnlyLetters2(S):
    letter = [c for c in S if c.isalpha()]
    ans = []
    for c in S:
        if c.isalpha():
            ans.append(letter.pop())
        else:
            ans.append(c)
    
    return ''.join(ans)
        