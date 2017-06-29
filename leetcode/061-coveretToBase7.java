public static String convertToBase7(int num) {
    String res = "";
    while (Math.abs(num) >= 7) {
        res = (Math.abs(num) % 7) + res;
        num /= 7;
    }
    return num + res;
}

//recursive
public static String convertToBase7(int num) {
    if (num < 0) return "-" + convertToBase7(-num);
    if (num < 7) return num + "";
    return convertToBase7(num / 7) + num % 7;
}
