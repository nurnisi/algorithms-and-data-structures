def losslessDataCompression(inputString, width):
    compr = []
    n, i = len(inputString), 0

    while i < n:
        windowStart = max(0, i-width)
        minStartIdx, length = None, 0
        for startIdx in range(windowStart, i):
            curIdx, j = startIdx, i
            while curIdx < i and j < n and inputString[curIdx] == inputString[j]:
                curIdx += 1
                j += 1
            if j - i > length:
                minStartIdx = startIdx
                length = j - i
        if minStartIdx != None:
            compr.append(str.format('({},{})', minStartIdx, length))
            i += length
        else:
            compr.append(inputString[i])
            i += 1
    
    return ''.join(compr)

print(losslessDataCompression('abacabadabacaba', 7))