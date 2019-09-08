def optimal(a, b, target):
    def binary(arr, x, target):
        l, r = 0, len(arr)
        while l < r:
            m = (l+r)//2
            if arr[m][1] + x <= target: l = m+1
            else: r = m
        return l

    ans = []
    max_sum = 0
    a = sorted(a, key=lambda elem: elem[1])

    for id_, val in b:
        i = binary(a, val, target)
        if i == 0: continue

        sum_ = val+a[i-1][1]

        if sum_ > max_sum:
            ans = []
            max_sum = sum_

        if sum_ == max_sum:
            while i > 0 and val+a[i-1][1] == max_sum:
                ans.append([a[i-1][0], id_])
                i -= 1

    return ans

# print(optimal([[1, 2], [2, 4], [3, 6]], [[1, 2]], 7))
# print(optimal([[1, 7], [2, 7], [3, 7]], [[1, 7]], 14))
print(optimal([[1, 3], [2, 5], [3, 7], [4, 10]], [[1, 2], [2, 3], [3, 4], [4, 5]], 10))