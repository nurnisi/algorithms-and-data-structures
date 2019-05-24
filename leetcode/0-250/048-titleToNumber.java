public static int titleToNumber(String s) {
    char[] arr = s.toCharArray();
    int res = 0;
    for (int i = 0; i < arr.length; i++) {
        res += Math.pow(26, arr.length - i - 1) * (arr[i] - 'A' + 1);
    }
    return res;
}
