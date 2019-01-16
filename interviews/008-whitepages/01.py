# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def readInput():
    canyon = []
    for line in sys.stdin:
        try:
            i = int(line)
            canyon.append(i)
        except ValueError:
            return []
    return canyon

def dragonChallenge():
    # check the input
    canyon = readInput()
    if not canyon or not len(canyon):
        print("failure")
        return

    # greedily identify optimal jumps
    n = len(canyon)
    path = [0] * (n + 1)
    j = 1
    for i in range(n):
        if j <= i: 
            j = i + 1
        while j < n + 1 and j < i + canyon[i] + 1:
            if not path[j]: path[j] = path[i] + 1
            else: path[j] = min(path[j], path[i] + 1)
            j += 1
        if j >= n + 1:
            break
    
    # print the output
    out = []
    for i in range(1, n + 1):
        if not path[i]:
            print("failure")
            return
        if path[i - 1] != path[i]:
            out.append(str(i - 1))

    out.append("out")
    print(", ".join(out))

dragonChallenge()