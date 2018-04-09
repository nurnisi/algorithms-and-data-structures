public static String toHex(int num) {
    StringBuilder res = new StringBuilder();
    while (num > 0) {
        int k = num % 16;
        if (k < 10) res.append(k);
        else res.append((char) (k + 87));
        num /= 16;
    }

    return res.reverse().toString();
}

//bit operations
public static String toHexBit(int num) {
    if (num == 0) return "0";
    StringBuilder res = new StringBuilder();

    while (num != 0 && res.length() != 8) {
        int runner = 0, k = 0;
        while (runner < 4) {
            if ((num & 1) == 1) k += Math.pow(2, runner);
            num = num>>1;
            runner++;
        }
        if (k < 10) res.append(k);
        else res.append((char) (k + 87));
    }

    return res.reverse().toString();
}
