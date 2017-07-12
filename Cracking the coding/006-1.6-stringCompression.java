public static String stringCompression(String s) {
    StringBuilder sb = new StringBuilder();
    int counter = 1;
    for (int i = 0; i < s.length() - 1; i++) {
        if (s.charAt(i) != s.charAt(i + 1)) {
            sb.append(s.charAt(i));
            sb.append(counter);
            counter = 1;
        } else {
            counter++;
        }
    }

    sb.append(s.charAt(s.length() - 1));
    sb.append(counter);

    String res = sb.toString();
    return s.length() <= res.length() ? s : res;
}
