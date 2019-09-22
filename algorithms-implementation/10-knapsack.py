# Fractional Knapsack
"""
Given weights and values of n items, we need to put these items
in a knapsack of capacity W to get the maximum total value in the knapsack.

items = {{60, 10}, {100, 20}, {120, 30}} => (value, weight)
W = 50;
"""

# Greedy
def knapsack_fractional(items, W):
    cap = val = 0
    
    for v, w in sorted(items, key=lambda x: x[0]/x[1], reverse=True):
        if cap + w >= W:
            return val + v//w * (W - cap)
        val, cap = val+v, cap+w
    
    return val

wt = [10, 40, 20, 30] 
val = [60, 40, 100, 120] 
capacity = 50

print(knapsack_fractional(zip(val, wt), capacity))
    

            

        

