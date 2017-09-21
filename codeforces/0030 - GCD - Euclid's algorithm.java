// recursive
static int gcd(int a, int b) {
    System.out.println(a + " " + b);
    if (b == 0) return  a;
    return gcd(b, a % b);
}

