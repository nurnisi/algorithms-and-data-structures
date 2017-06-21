public static String convertToTitle(int n) {
    String res = "";
    while(n != 0) {
        int i = n % 26;
        char ch = i == 0 ? 'Z' : (char) (i + 64);
        res = ch + res;
        n = i == 0 ? n / 26 - 1 : n / 26;
    }
    return res;
}
