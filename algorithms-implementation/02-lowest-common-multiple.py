class lcm:
    def lcm(self, n, m):
        return n * m // self.gcd(n, m)

    # non-recursive
    def gcd(self, n, m):
        while m > 0:
            n, m = m, n % m
        return n

    # recursive
    def gcd_rec(self, n, m):
        if m == 0: return n
        return self.gcd_rec(m, n % m)

lcm = lcm()
print(lcm.gcd(10, 15))
print(lcm.gcd_recursive(10, 15))
print(lcm.lcm(10, 15))