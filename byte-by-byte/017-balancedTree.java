private class Node {
  private int value;
  private Node left;
  private Node right;
}

public static boolean isBalanced(Node n) {
  if(balancedHeight(n) > -1) return true;
  return false;
}

private int balancedHeight(Node n) {
  if(n == null) return 0;
  int h1 = balancedHeight(n.left);
  int h2 = balancedHeight(n.right);

  if(h1 == -1 || h2 == -1) return -1;
  if(Math.abs(h1-h2) > 1) return -1;
  if(h1 > h2) return h1 + 1;
  return h2 + 1;
}
