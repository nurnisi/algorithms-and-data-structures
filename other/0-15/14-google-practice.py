def houses_stores(houses, stores):
    stores = sorted(stores)
    n = len(stores)
    
    def binary(x):
        l, r = 0, n
        while l < r:
            m = (l+r)//2
            if stores[m] < x:
                l = m + 1
            else:
                r = m
        return l

    ans = []
    for h in houses:
        i = binary(h)

        left = stores[i-1] if i > 0 else float('-inf')
        right = stores[i] if i < n else float('inf')
        
        ans.append(left if h - left <= right - h else right)

    return ans

houses = [0, 5, 10, 17, 30]
stores = [1, 5, 11, 16, 20]

houses = [2, 4, 2]
stores = [5, 1, 2, 3]

houses = [4, 8, 1, 1]
stores = [5, 3, 1, 2, 6]

print(houses_stores(houses, stores))