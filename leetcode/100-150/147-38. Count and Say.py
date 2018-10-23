# 38. Count and Say
def countAndSay(n):
    s = "1"
    for _ in range(n - 1):
        res = ""
        prev = ""
        count = 0
        for ch in s:
            if prev != ch:
                if count: 
                    res += (str(count) + prev)
                prev = ch
                count = 0
            count += 1
        res += (str(count) + prev)
        s = res
    return s

print(countAndSay(8))