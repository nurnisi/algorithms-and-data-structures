// recursive
static int gcd(int a, int b) {
    System.out.println(a + " " + b);
    if (b == 0) return  a;
    return gcd(b, a % b);
}

// non-recursive
static int gcd(int a, int b) {
    while (b > 0) {
        int temp = a;
        a = b;
        b = temp % b;
    }
    return a;
}