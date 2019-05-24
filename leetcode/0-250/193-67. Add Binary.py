# 67. Add Binary
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        lena, lenb = len(a), len(b)
        maxlen = max(lena, lenb)
        arr = [0] * maxlen
        i, c = 0, 0
        while i < lena and i < lenb:
            c += int(a[lena-i-1]) + int(b[lenb-i-1])
            arr[i] = str(c & 1)
            c >>= 1
            i += 1
        
        while i < lena:
            c += int(a[lena-i-1])
            arr[i] = str(c & 1)
            c >>= 1
            i += 1
        
        while i < lenb:
            c += int(b[lenb-i-1])
            arr[i] = str(c & 1)
            c >>= 1
            i += 1

        if c: arr += [str(c)]
        arr.reverse()
        return ''.join(arr)

    def addBinary2(self, a, b):
        ans, i, c, lena, lenb = "", 0, 0, len(a), len(b)
        while i < lena or i < lenb:
            if i < lena: c += int(a[lena - i - 1])
            if i < lenb: c += int(b[lenb - i - 1])
            ans = str(c & 1) + ans
            c >>= 1
            i += 1
        
        if c: ans = str(c) + ans
        return ans

sol = Solution()
print(sol.addBinary("11", "1"))

        