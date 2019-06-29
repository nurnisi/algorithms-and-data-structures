# Next permutation
def nextPermutation(self, n: int) -> int:
    digits = list(str(n))
    i, j = len(digits)-2, len(digits)-1

    # Find the first digit that is smaller than the digit next to it
    while i >= 0 and digits[i] >= digits[i+1]:
        i -= 1
    
    # If not found, then all digits are in descending order 
    if i == -1: return -1

    # Find the smallest digit on right side greatee than the found number
    while digits[j] <= digits[i]:
        j -= 1

    # Swap
    digits[i], digits[j] = digits[j], digits[i]

    # Reverse
    res = int("".join(digits[:i+1] + digits[i+1:][::-1]))

    if res >= 2**31 or res == n: return -1
    return res