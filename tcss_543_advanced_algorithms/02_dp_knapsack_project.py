# bottom-up dp: traverses iteratively starting from the smallest subset (bottom) going up
# ex: fib(1), fib(2), fib(3), fib(4), ... , fib(n)
def knapsack_bottom_up_dp(weights, values, W):
    # generating array for storing optimal values
    n = len(weights)
    opt_vals = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    # computing possible optimal values
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            wi = weights[i - 1]
            # when weight of the current item is greater than current weight
            # take the previous optimal value from top
            if wi > w:
                opt_vals[i][w] = opt_vals[i - 1][w]
            # otherwise, take the maximum between:
            # putting the current item or taking the previous selection
            else:
                opt_vals[i][w] = max(values[i - 1] + opt_vals[i - 1][w - wi], opt_vals[i - 1][w])

    # backtracking
    opt_subset = [0 for i in range(n)]
    i, w = n, W
    while i > 0 and w > 0:
        wi = weights[i - 1]
        if opt_vals[i][w] == values[i - 1] + opt_vals[i - 1][w - wi]:
            opt_subset[i - 1] = 1
            w -= wi
        i -= 1    

    for i in opt_vals: print(i)
    return (opt_vals[-1][-1], opt_subset)

# top-down: recursively computes values starting from the biggest (top) going down
# ex: fib(n), fib(n-1), fib(n-2), ... , fib(1)
def knapsack_top_down_dp(weights, values, W):
    # generating array for storing optimal values
    n = len(weights)
    opt_vals = [[0 for _ in range(W + 1)]]
    [opt_vals.append([0 if j == 0 else -1 for j in range(W + 1)]) for _ in range(n)]

    # run recursion
    max_val = helper(weights, values, opt_vals, n, W)

    # backtracking
    opt_subset = [0 for i in range(n)]
    i, w = n, W
    while i > 0 and w > 0:
        wi = weights[i - 1]
        if opt_vals[i][w] == values[i - 1] + opt_vals[i - 1][w - wi]:
            opt_subset[i - 1] = 1
            w -= wi
        i -= 1  

    for i in opt_vals: print(i)
    return (max_val, opt_subset)

def helper(weights, values, opt_vals, i, w):
    # base case
    if opt_vals[i][w] >= 0:
        return opt_vals[i][w]

    # skip the item if the wieght of item is bigger than the remaining weight in the knapsack
    if weights[i - 1] > w :
        max_val = helper(weights, values, opt_vals, i - 1, w)
    # otherwise, recursively compute maximum between picking the item or not picking the item
    else:
        max_val = max(values[i - 1] + helper(weights, values, opt_vals, i - 1, w - weights[i - 1]),
                      helper(weights, values, opt_vals, i - 1, w))
    
    # memorize the computed maximum value
    opt_vals[i][w] = max_val
    return max_val

# brute force: generate all possible 2^n variants and determine the maximum optimal value
import itertools
def knapsack_brute_force(weights, values, W):
    # initializing length, maximum total value and optimal subset of selected items
    n, max_val, opt_subset = len(weights), 0, []

    # generating all possible combinations of selecting n items
    combinations = map(list, itertools.product([0, 1], repeat=n))

    # iterating over all combinations
    for cmb in combinations:
        # calcualting total weight and total value for current combination
        tot_weights = sum([a*b for a,b in zip(weights, cmb)])
        tot_values = sum([a*b for a,b in zip(values, cmb)])

        # updating maximum total value and optimal subset to current
        if tot_weights <= W and tot_values > max_val:
            max_val = tot_values
            opt_subset = cmb
    
    return (max_val, opt_subset)

def main():
    print("BOTTOM UP:")
    print(knapsack_bottom_up_dp([2,2,3], [2,3,4], 6))
    print(knapsack_bottom_up_dp([2,2,3], [7,2,1], 6))

    print("TOP DOWN:")
    print(knapsack_top_down_dp([2,2,3], [2,3,4], 6))
    print(knapsack_top_down_dp([2,2,3], [7,2,1], 6))

    print("BRUTE FORCE:")
    print(knapsack_brute_force([2,2,3], [2,3,4], 6))
    print(knapsack_brute_force([2,2,3], [7,2,1], 6))

# main()

import random
# print(random.sample(range(200), 100))
# print(random.sample(range(300), 100))
n = 24
print(knapsack_brute_force(random.sample(range(n * 10), n),random.sample(range(n * 10), n), 1000))
