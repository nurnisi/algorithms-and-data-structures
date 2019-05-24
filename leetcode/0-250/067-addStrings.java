public static String addStrings(String num1, String num2) {
    int l1 = num1.length() - 1, l2 = num2.length() - 1, tens = 0;
    String res = "";
    while (l1 >= 0 && l2 >= 0) {
        int a = (int) num1.charAt(l1--) - 48;
        int b = (int) num2.charAt(l2--) - 48;
        int sum = a + b + tens;
        int digits = sum % 10;
        res = digits + res;
        tens = sum / 10;
    }

    while (l1 >= 0) {
        int a = (int) num1.charAt(l1--) - 48;
        int digits = (a + tens) % 10;
        res = digits + res;
        tens = (a + tens) / 10;
    }

    while (l2 >= 0) {
        int a = (int) num2.charAt(l2--) - 48;
        int digits = (a + tens) % 10;
        res = digits + res;
        tens = (a + tens) / 10;
    }
}
