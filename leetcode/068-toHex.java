public static String toHex(int num) {
    if (num < 0) num = ~(-num) + 1;
    StringBuilder res = new StringBuilder();
    while (num > 0) {
        int k = num % 16;
        if (k < 10) res.append(k);
        else res.append((char) (k + 87));
        num /= 16;
    }

    return res.reverse().toString();
}

//binary
