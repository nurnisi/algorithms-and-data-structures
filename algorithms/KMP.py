# takes a string and a pattern as inputs
class KMP:
    def matchPattern(self, s, p): 
        N, M = len(s), len(p)

        # longest prefix suffix
        lps = [0] * M
        self.calculateLPS(p, M, lps)

        i, j, matches = 0, 0, []
        while i < N:
            if p[j] == s[i]:
                i += 1
                j += 1
            
            if j == M:
                matches.append(i - j)
                j = lps[j - 1]

            elif i < N and p[j] != s[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return matches


    def calculateLPS(self, p, M, lps):
        len = 0 # length of the previous longest refix suffix
        lps[0] = 0
        i = 1

        while i < M:
            if p[i] == p[len]:
                len += 1
                lps[i] = len
                i += 1
            else:
                if len != 0:
                    len = lps[len - 1]
                else:
                    lps[i] = 0
                    i += 1

kmp = KMP()
print(kmp.matchPattern("AAAAABAAABA", "AAAA"))