private static int BITS_IN_INTEGER = 32;

public int rotateClockwise(int x, int N) {
  N = N % BITS_IN_INTEGER;
  return (x >> N | x << (BITS_IN_INTEGER - N));
}

public int rotateCounterClockwise(int x, int N) {
  N = N % BITS_IN_INTEGER;
  return (x << N | x >> (BITS_IN_INTEGER - N));
}
