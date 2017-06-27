public static int longestPalindrome(String s) {
    char[] arr = s.toCharArray();
    Arrays.sort(arr);
    int res = 0;
    for (int i = 1; i < arr.length; i++) {
        if (arr[i - 1] == arr[i]) {
            res += 2;
            i += 1;
        }
    }
    return res + (res < arr.length ? 1 : 0);
}
