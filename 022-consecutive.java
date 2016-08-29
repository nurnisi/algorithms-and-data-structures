public class Node {
  int value;
  Node left;
  Node right;
}

public static int consecutive(Node n) {
  if(n == null) return 0;
  return max(consecutive(n.left, n.value, 1), consecutive(n.right, n.value, 1));
}

private int consecutive(Node n, int prev, int length) {
  if(n == null) return length;
  if(n.value == prev + 1) {
    int leftLength = consecutive(n.left, n.value, length + 1);
    int rightLength = consecutive(n.right, n.value, length + 1);
    return max(leftLength, rightLength);
  } else {
    int leftLength = consecutive(n.left, n.value, 1);
    int rightLength = consecutive(n.right, n.value, 1);
    return max(leftLength, rightLength, length);
  }
}

private int max(int... vals) {
  int max = Integer.MIN_VALUE;
  for(int x : vals) {
    if(x > max) max = x;
  }
  return max;
}
