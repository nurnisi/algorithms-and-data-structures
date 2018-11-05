def knapsack(weights, values, W):
    vals = [[0 for _ in range(W + 1)] for _ in range(len(weights) + 1)]
    
    for i in range(1, len(vals)):
        for w in range(1, len(vals[0])):
            wi = weights[i - 1]
            if wi > w:
                vals[i][w] = vals[i - 1][w]
            else:
                vals[i][w] = max(values[i - 1] + vals[i - 1][w - wi], vals[i - 1][w])

    for i in vals: print(i)

    return vals[-1][-1]

knapsack([2,2,3], [2,3,4], 6)