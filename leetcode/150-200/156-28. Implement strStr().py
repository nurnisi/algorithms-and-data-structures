# 28. Implement strStr()
class Solution(object):
    # brute-force 1
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lh , ln = len(haystack), len(needle)
        if ln == 0: return 0
        for i in range(lh - ln + 1):
            j = 0
            while j < ln:
                if haystack[i + j] != needle[j]: break
                j += 1
            if j == ln:
                return i
        
        return -1

    # brute-force 2
    def strStr1(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lh, ln = len(haystack), len(needle)
        for i in range(lh - ln + 1):
            if haystack[i : (i+ln)] == needle:
                return i
        return -1

    # KMP
    def strStr2(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        N, M = len(haystack), len(needle)
        if not N and not M:
            return 0
        if not N:
            return -1
        if not M:
            return 0
        
        # longest prefix suffix
        lps = [0] * M
        self.calculateLPS(needle, M, lps)

        i, j, matches = 0, 0, []
        while i < N:
            if needle[j] == haystack[i]:
                i += 1
                j += 1
            
            if j == M:
                matches.append(i - j)
                j = lps[j - 1]

            elif i < N and needle[j] != haystack[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return matches[0] if matches else -1

    def calculateLPS(self, needle, M, lps):
        len = 0 # length of the previous longest refix suffix
        lps[0] = 0
        i = 1

        while i < M:
            if needle[i] == needle[len]:
                len += 1
                lps[i] = len
                i += 1
            else:
                if len != 0:
                    len = lps[len - 1]
                else:
                    lps[i] = 0
                    i += 1

    # Z-algorithm
    def strStr3(self, haystack, needle):
        N, M = len(haystack), len(needle)
        if not N and not M:
            return 0
        if not N:
            return -1
        if not M:
            return 0
        
        s = needle + "$" + haystack
        z = self.calculateZ(s)
        res = []
        for i in range(len(z)):
            if z[i] == len(needle):
                res.append(i - len(needle) - 1)
        return res[0] if res else -1
    
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

        