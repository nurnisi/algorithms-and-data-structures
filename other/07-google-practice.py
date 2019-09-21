def func2(A, k):
    return A[A.index(max(A[:-k+1])):][:k]

def func(A, k):
    max_elem = max(A[:-k+1]) # get max element
    i = A.index(max_elem) # get it's index
    return A[i: k+i]

A = [1, 4, 3, 2, 5]
print(func(A, 4))