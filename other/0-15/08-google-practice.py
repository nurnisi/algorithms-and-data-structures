def func(plants, capacity):
    steps = cur = 0
    for i, x in enumerate(plants):
        if cur + x > capacity:
            steps += i * 2
            cur = 0
        steps += 1
        cur += x
    return steps

print(func([2, 4, 5, 1, 2], 6))