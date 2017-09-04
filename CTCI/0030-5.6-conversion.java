static int conversion(int num1, int num2) {
    int res = 0;
    for (int i = 0; i < Integer.BYTES * 8; i++) {
        if ((num1 & 1) != (num2 & 1)) res++;
        num1 >>= 1;
        num2 >>= 1;
    }
    return res;
}