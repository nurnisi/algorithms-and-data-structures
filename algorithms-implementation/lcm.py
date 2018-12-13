class lcm:
    def lcm(self, n, m):
        return n * m // self.gcd(n, m)

    # non-recursive
    def gcd(self, n, m):
        while m > 0:
            n, m = m, n % m
        return n

    # recursive
    def gcd_recursive(self, n, m):
        return n if m == 0 else self.gcd_recursive(m, n % m)

lcm = lcm()
print(lcm.gcd(10, 15))
print(lcm.gcd_recursive(10, 15))
print(lcm.lcm(10, 15))