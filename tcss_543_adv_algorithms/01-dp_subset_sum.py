def subset_sum(items, W):
    sums = [[0 for _ in range(W + 1)] for _ in range(len(items) + 1)]
    for i in range(1, len(sums)):
        for w in range(1, len(sums[0])):
            wi = items[i - 1]
            if wi > w:
                sums[i][w] = sums[i - 1][w]
            else:
                sums[i][w] = max(sums[i - 1][w], sums[i - 1][w - wi] + wi)
    
    for i in sums: print(i)

    return sums[len(sums) - 1][W]

subset_sum([2,2,3], 6)