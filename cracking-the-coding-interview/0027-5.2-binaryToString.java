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

//CTCI
public static String binaryToString(double num) {
  if (num >= 1 || num <= 0) return "ERROR";

  StringBuilder binary = new StringBuilder();
  binary.append(".");
  while (num > 0) {
    if (binary.length() >= 32) return "ERROR";

    double m = num * 2;
    if (m > 1) {
      binary.append(1);
      num = m - 1;
    } else {
      binary.append(0);
      num = m;
    }
  }

  return binary.toString();
}

//CTCI 2
public static String binaryToString(double num) {
  if (num >= 1 || num <= 0) return "ERROR";

  StringBuilder binary = new StringBuilder();
  binary.append(".");
  double fraction = 0.5;

  while (num > 0) {
    if (binary.length() >= 32) return "ERROR";

    if (num >= fraction) {
      num -= fraction;
      binary.append(1);
    } else binary.append(0);
    frac /= 2;
  }

  return binary.toString();
}
