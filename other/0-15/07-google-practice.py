def func2(A, k):
    return A[A.index(max(A[:-k+1])):][:k]

def func(A, k):
    max_elem = max(A[:-k+1]) # get max element
    i = A.index(max_elem) # get it's index
    return A[i: k+i]

def largest_subarray(A, k):
    cum = [A[0]]
    div = 10**(k-1)
    for i in range(1, len(A)):
        cum.append(cum[-1]%div*10 + A[i])
    
    return A[cum.index(max(cum))-k+1:][:k]

A = [1, 4, 4, 4, 4, 4]
print(largest_subarray(A, 4))