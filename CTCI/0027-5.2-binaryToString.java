public static String binaryToString(double num) {
  String res = "";
  while (num != 1) {
    double m = num * 2;
    res += Double.toInteger(m);
    num = m;
    if (res.length() == 32) return "ERROR";
  }
  return res;
}
