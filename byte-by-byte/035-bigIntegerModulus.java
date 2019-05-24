public static int mod(byte[] a, int b) {
  int m = 0;
  for(int i = 0; i < a.length; i++) {
    m <<= 8;
    m += (a[i] & 0xFF);
    m %= b;
  }

  return m;
}
