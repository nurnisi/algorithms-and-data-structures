public static int getSum(int a, int b) {
    int res = 0, c = 0;
    for(int i = 0; i < 32; i++) {
        int x = a >> i & 1;
        int y = b >> i & 1;
        int d = c == 0 ? (x ^ y) : (c ^ x ^ y);
        res |=  d << i;
        c = c == 0 ? (x & y) : (x | y);
    }
    return res;
}
