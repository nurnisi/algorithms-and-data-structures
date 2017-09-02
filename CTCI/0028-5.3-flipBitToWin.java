public static int flipBitToWin(int num) {
    int c1 = 0, c2 = 0, zeros = 0, max = Integer.MIN_VALUE;
    for (int i = 0; i < 32; i++) {
        if ((num & 1) == 0) {
            zeros++;
            if (c2 != 0) {
                max = Math.max(max, c1 + c2 + 1);
                c1 = c2;
                c2 = 0;
                zeros = 1;
            } else if (zeros > 1) {
                max = Math.max(max, c1 + 1);
                c1 = 0;
            }
        } else {
            if (c1 == 0) zeros = 0;
            if (zeros == 0) c1++;
            else if (zeros == 1) c2++;
        }
        num >>= 1;
    }
    return max;
}