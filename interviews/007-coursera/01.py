def mystery(letter):
    ans = []
    for let in letter:
        left, right = 0, len(let)-1
        count = 0
        while left < right:
            count += abs(ord(let[left]) - ord(let[right])
            left += 1
            right -= 1
        ans.append(count)
    return ans