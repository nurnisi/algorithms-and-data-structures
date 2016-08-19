private static int BITS_IN_INTEGER = 32;

public int rotateClockwise(int x, int N) {
  return (x >> N | x << (BITS_IN_INTEGER - N));
}

public int rotateCounterClockwise(int x, int N) {
  return (x << N | x >> (BITS_IN_INTEGER - N));
}
