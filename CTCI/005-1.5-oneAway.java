public static boolean oneAway(String str1, String str2) {
    if (Math.abs(str1.length() - str2.length()) > 1) return false;
    int counter = 0, runner1 = 0, runner2 = 0;
    while (runner1 < str1.length() && runner2 < str2.length()) {
        if (str1.charAt(runner1) != str2.charAt(runner2)) {
            counter++;
            if (str1.length() > str2.length()) runner1++;
            else if (str1.length() < str2.length()) runner2++;
            else {
                runner1++;
                runner2++;
            }
        } else {
            runner1++;
            runner2++;
        }
        if (counter > 1) return false;
    }
    return true;
}
