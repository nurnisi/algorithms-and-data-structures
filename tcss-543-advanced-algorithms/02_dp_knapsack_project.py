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
            # if weight of the current item is greater than the current weight
            # take the previous optimal value from previous top slot (i - 1)
            if wi > w:
                opt_vals[i][w] = opt_vals[i - 1][w]
            # otherwise, take the maximum between:
            # putting the current item into the knapsack or not
            else:
                opt_vals[i][w] = max(values[i - 1] + opt_vals[i - 1][w - wi], 
                                     opt_vals[i - 1][w])

    # backtracking
    opt_subset = backtrack(n, W, weights, values, opt_vals)

    # for i in opt_vals: print(i)
    return (opt_vals[-1][-1], opt_subset)

# top-down: recursively computes values starting from the biggest (top) going down
# ex: fib(n), fib(n-1), fib(n-2), ... , fib(1)
def knapsack_top_down_dp(weights, values, W):
    # generating array for storing optimal values with 0 in edges and -1 elsewhere
    n = len(weights)
    opt_vals = [[0 for _ in range(W + 1)]]
    [opt_vals.append([0 if j == 0 else -1 for j in range(W + 1)]) for _ in range(n)]

    # run recursion
    max_val = helper(weights, values, opt_vals, n, W)

    # backtracking
    opt_subset = backtrack(n, W, weights, values, opt_vals)

    # for i in opt_vals: print(i)
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

def backtrack(n, W, weights, values, opt_vals):
    opt_subset = [0 for i in range(n)]
    i, w = n, W
    while i > 0 and w > 0:
        wi = weights[i - 1]
        if w - wi >= 0 and opt_vals[i][w] == values[i - 1] + opt_vals[i - 1][w - wi]:
            opt_subset[i - 1] = 1
            w -= wi
        i -= 1 
    return opt_subset

# brute force: generate all possible 2^n variants and determine the maximum optimal value
# brute force: without bit manipulation
import itertools
def knapsack_brute_force(weights, values, W):
    # initializing length, maximum total value and optimal subset of selected items
    n, max_val, opt_subset = len(weights), 0, []

    # creating a generator, that traveses through all possible combinations of selecting n items
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

# brute force: with bit manipulation
def knapsack_brute_force_bm(weights, values, W):
    # initializing length, maximum total value and optimal subset of selected items
    n, max_val = len(weights), 0
    opt_subset = [0]*n
    i, m = 1, 2**n

    # iterating over all combinations
    while i < m:
        j, tot_weights, tot_values, cur = i, 0, 0, 0
        cur_subset = [0]*n
        while j:
            if j & 1:
                tot_weights += weights[cur]
                tot_values += values[cur]
                cur_subset[cur] = 1
            j >>= 1
            cur += 1
        i+=1
        
        # updating maximum total value and optimal subset to current 
        if tot_weights <= W and tot_values > max_val:
            max_val = tot_values
            opt_subset = cur_subset
    
    return (max_val, opt_subset)

# correctness testing
def corr_test():
    functions = [
        ("BOTTOM UP:", knapsack_bottom_up_dp), 
        ("TOP DOWN:", knapsack_top_down_dp),
        ("BRUTE FORCE:", knapsack_brute_force),
        ("BRUTE FORCE (bit manip.):", knapsack_brute_force_bm)
    ]

    # source of the test cases: http://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html
    test_cases = [
        [([2,2,3], [2,3,4], 6), [0, 1, 1]],
        [([2,2,3], [7,2,1], 6), [1, 1, 0]],
        [([23,31,29,44,53,38,63,85,89,82], [92,57,49,68,60,43,67,84,87,72], 165), [1,1,1,1,0,1,0,0,0,0]],
        [([12,7,11,8,9], [24,13,23,15,16], 26), [0,1,1,1,0]],
        [([56,59,80,64,75,17], [50,50,64,46,50,5], 190), [1,1,0,0,1,0]],
        [([31,10,20,19,4,3,6], [70,20,39,37,7,5,10], 50), [1,0,0,1,0,0,0]],
        [([25,35,45,5,25,3,2,2], [350,400,450,20,70,8,5,5], 104), [1,0,1,1,1,0,1,1]],
        [([41,50,49,59,55,57,60], [442,525,511,593,546,564,617], 170), [0,1,0,1,0,0,1]]
    ]
    for fn in functions:
        for tc in test_cases:
            max_val, opt_subset = fn[1](*tc[0])
            is_correct = opt_subset == tc[1]
            print(fn[0], max_val)
            print("Correct:", is_correct)
            print("Output:", opt_subset)
            print("Answer:", tc[1])

import random
import time
import numpy as np
import pandas as pd

def main():
    # Brute force vs. DP bottom-up vs. DP top-down
    test(*get_inputs_BF_vs_DPbu_vs_DPtd())

    # DP bottom-up vs. DP top-down
    test(*get_inputs_DPbu_vs_DPtd())
    
# generate inputs for testing DP bottom-up vs. DP top-down
def get_inputs_BF_vs_DPbu_vs_DPtd():
    # N = np.arange(1, 26, 1)         #[1, 2, ..., 25]
    # K = np.arange(0.2, 1.1, 0.2)    #[0.1, 0.2, ..., 1]
    # wi_vi_pow = np.arange(3, 10, 2)  #[3, 5, 7, 9]
    N = np.arange(1, 3, 1)         #[1, 2, ..., 25]
    K = np.arange(0.2, 0.3, 0.2)    #[0.1, 0.2, ..., 1]
    wi_vi_pow = np.arange(3, 4, 2)  #[3, 5, 7, 9]
    algorithms = [
        ("Brute force", knapsack_brute_force), 
        ("DP bottom-up",knapsack_bottom_up_dp),
        ("DP top-down", knapsack_top_down_dp)
    ]
    filename = "DP bottom-up vs. DP top-down"
    return (N, K, wi_vi_pow, algorithms, filename)

# generate inputs for testing DP bottom-up vs. DP top-down
def get_inputs_DPbu_vs_DPtd():
    # N = [2**i for i in range(0,32)]
    # K = np.arange(0.2, 1.1, 0.2)
    # wi_vi_pow = np.arange(3, 10, 2)
    N = [2**i for i in range(0,2)]
    K = np.arange(0.2, 0.3, 0.2)
    wi_vi_pow = np.arange(3, 4, 2)
    algorithms = [
        ("DP bottom-up", knapsack_bottom_up_dp),
        ("DP top-down", knapsack_top_down_dp)
    ]
    filename = "DP bottom-up vs. DP top-down"
    return (N, K, wi_vi_pow, algorithms, filename)
    
# full testing
def test(N, K, wi_vi_pow, algorithms, filename):
    # arrays to store columns of the output table
    runtimes = [[] for _ in algorithms]
    n_arr = []
    W_arr = []
    wi_vi_range_arr = []

    # run over all combinations of the inputs
    # different number of input items 
    for ni in N:
        # different range of weights and values (ni = n) => 1,2,3,...,n
        for wi_vi in wi_vi_pow:
            # generate weights and values and compute sum of weights 
            # (range = (1, 10^wi_vi)) => (1, 10^3),...,(1, 10^m)
            weights = np.random.randint(10**wi_vi, size=ni)
            values = np.random.randint(10**wi_vi, size=ni)
            sum_weights = sum(weights)
            # different capacity of the knapsack 
            # (W = sum(weights) * ki) => W*1,W*0.8,...,W*0.2
            for ki in K:
                # add inputs values into the table columns           
                n_arr.append(ni)
                W_arr.append(int(sum_weights * ki))
                wi_vi_range_arr.append(10**wi_vi)
                # run algorithms and time performance
                print("Inputs: n={}, W={}".format(ni, W_arr[-1]))
                for i in range(len(algorithms)):
                    print("Running: {} with wi_vi_range: 1-{}".format(algorithms[i][0], wi_vi_range_arr[-1]))
                    start = time.clock()
                    algorithms[i][1](weights, values, int(sum_weights * ki))
                    end = time.clock()
                    runtimes[i].append(end - start)
        # save table as csv            
        save(runtimes, algorithms, n_arr, W_arr, wi_vi_range_arr, filename)
    # save table as csv    
    save(runtimes, algorithms, n_arr, W_arr, wi_vi_range_arr, filename)                

# save table as csv
def save(runtimes, algorithms, n_arr, W_arr, wi_vi_range_arr, filename):
    total_runtime = sum([sum(rn) for rn in runtimes])
    print("Saving to csv\nTotal runtime: {}".format(total_runtime))
    df_algorithms = pd.concat([pd.Series(rn) for rn in runtimes], keys=[alg[0] for alg in algorithms], axis=1)
    df_inputs = pd.DataFrame({"n": n_arr, "W": W_arr, "wi, vi range": wi_vi_range_arr})
    df_concat = pd.concat([df_algorithms, df_inputs], axis = 1)
    df_concat.to_csv(filename+".csv")

if __name__ == "__main__":
    main()