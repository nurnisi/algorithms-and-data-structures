static int conversion(int num1, int num2) {
    int res = 0;
    for (int i = 0; i < Integer.BYTES * 8; i++) {
        if ((num1 & 1) != (num2 & 1)) res++;
        num1 >>= 1;
        num2 >>= 1;
    }
    return res;
}

//CTCI: 1
static int conversion(int num1, int num2) {
    int count = 0;
    for (int c = num1 ^ num2; c != 0; c >>= 1) {
        count += c & 1;
    }
    return count;
}

//CTCI: 2
static int conversion(int num1, int num2) {
    int count = 0;
    for (int c = num1 ^ num2; c != 0; c = c & (c - 1)) {
        count++;
    }
    return count;
}