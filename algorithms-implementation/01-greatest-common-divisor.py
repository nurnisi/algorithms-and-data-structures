class gcd:
    # non-recursive
    def gcd_short(self, n, m):
        while m > 0:
            n, m = m, n % m
        return n

    # recursive
    def gcd_rec(self, n, m):
        if m == 0: return n
        return self.gcd_rec(m, n % m)
    
    def gcd_rec_short(self, n, m):
        return n if m == 0 else self.gcd_rec_short(m, n % m)

gcd = gcd()
print(gcd.gcd(10, 15))
print(gcd.gcd_rec(10, 15))
print(gcd.gcd_short(10, 15))
print(gcd.gcd_rec_short(10, 15))