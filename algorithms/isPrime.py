class isPrime:
    def isPrime(self, n):
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True
    
ip = isPrime()
print(ip.isPrime(5))