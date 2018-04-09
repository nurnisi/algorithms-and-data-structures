public static boolean checkRecord(String s) {
    int i = 0, a = 0, l = 0;
    while (i < s.length()) {
        if (s.charAt(i) == 'L') l++;
        else l = 0;

        if (s.charAt(i) == 'A') a++;

        if (l > 2) return false;
        if (a > 1) return false;
        i++;
    }
    return true;
}
