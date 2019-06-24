# Z-algorithm
class ZAlgorithm:
    def calculateZ(self, s):
        z = [0 for ch in s]
        left = right = 0
        for k in range(len(s)):
            if k > right:
                left = right = k
                while right < len(s) and s[right] == s[right - left]:
                    right += 1
                z[k] = right - left
                right -= 1
            else:
                k1 = k - left
                if z[k1] < right - k + 1:
                    z[k] = z[k1]
                else:
                    left = k
                    while right < len(s) and s[right] == s[right-left]:
                        right += 1
                    z[k] = right - left
                    right -= 1
        return z

    def matchPattern(self, text, pattern):
        s = pattern + "$" + text
        z = self.calculateZ(s)
        res = []
        for i in range(len(z)):
            if z[i] == len(pattern):
                res.append(i - len(pattern) - 1)
        return res
        

z = ZAlgorithm()
print(z.matchPattern("aaabcxyzaaaabczaaczabbaaaaaabc", "aaabc"))