#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closest' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#
import collections

def closest(s, queries):
    # create dictionary with indices of unique characters
    counts = collections.defaultdict(list)
    for i in range(len(s)):
        counts[s[i]].append(i)

    # populate ans array
    ans = []
    for q in queries:
        cnt = counts[s[q]]
        # binary search for index of query
        i = binarySearch(q, cnt)

        # find the closest or append -1
        if len(cnt) <= 1 or i == -1:
            ans.append(-1)
        elif i == 0:
            ans.append(cnt[i + 1])
        elif i == len(cnt) - 1:
            ans.append(cnt[i - 1])
        else:
            l, r = cnt[i - 1], cnt[i + 1]
            ans.append((r, l)[q - l <= r - q])

    return ans

def binarySearch(q, cnt):
    l, r = 0, len(cnt) - 1
    while l <= r:
        mid = (l + r) // 2
        if cnt[mid] < q:
            l = mid + 1
        elif cnt[mid] > q:
            r = mid - 1
        else:
            return mid
    return -1

print(closest("hackerrank", [4,1,6,8]))
print(closest("aabbccddee", [4,1,6,8]))
print(closest("a", [0]))
print(closest("aa", [0, 1]))
print(closest("aaaa", [0,1,2,3]))