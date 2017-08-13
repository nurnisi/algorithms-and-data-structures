public static int insertion(int N, int M, int i, int j) {
  int mask1 = -1 << (j + 1);
  int mask2 = (1 << i) - 1;
  int maskFinal = mask1 | mask2;

  int tempM = M << i;

  return N & maskFinal | tempM;
}
