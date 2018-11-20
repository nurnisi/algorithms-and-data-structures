def knapsack_bottom_up_dp(weights, values, W):
    # generating n by n array for storing optimal values
    n = len(weights)
    opt_vals = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    # traversing over optimal values
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            wi = weights[i - 1]
            # 
            if wi > w:
                opt_vals[i][w] = opt_vals[i - 1][w]
            else:
                opt_vals[i][w] = max(values[i - 1] + opt_vals[i - 1][w - wi], opt_vals[i - 1][w])

    for i in opt_vals: print(i)

    return opt_vals[-1][-1]

knapsack_bottom_up_dp([2,2,3], [2,3,4], 6)

import itertools
def knapsack_brute_force(weights, values, W):
    # initializing length, maximum total value and optimal subset of selected items
    n, max_tot_value, opt_subset = len(weights), 0, []

    # generating all possible combinations of selecting n items
    combinations = list(map(list, itertools.product([0, 1], repeat=n)))[1:]

    # iterating over all combinations
    for cmb in combinations:

        # calcualting total weight and total value for current combination
        tot_weights = sum([a*b for a,b in zip(weights, cmb)])
        tot_values = sum([a*b for a,b in zip(values, cmb)])

        # updating maximum total value and optimal subset to current
        if tot_weights <= W and tot_values > max_tot_value:
            max_tot_value = tot_values
            opt_subset = cmb
    
    return (max_tot_value, opt_subset)
        
knapsack_brute_force([2,2,3],[2,3,4], 6)