def generate(self, numRows):
    pt = []
    for i in range(numRows):
        lev = []
        lev.append(1)
        for j in range(1, i):
            lev.append(pt[i - 1][j] + pt[i - 1][j - 1])
        if i != 0: lev.append(1)
        pt.append(lev)
    return pt