//first
public static boolean gray(int a, int b) {
  int xor = a ^ b;

  return (xor & (xor - 1)) == 0;
}
//second
public static boolean gray2(int a, int b) {
  int xor = a ^ b;

  while(xor > 0) {
    if(xor % 2 == 1 && xor>>1 > 0) return false;
    xor = xor>>1;
  }

  return true;
}
