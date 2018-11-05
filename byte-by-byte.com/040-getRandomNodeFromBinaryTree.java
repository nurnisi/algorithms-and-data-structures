private class Node {
  Node left;
  Node right;
  int val;
  int children;
}

private Node root;
private Random rand;

public int getRandom() {
  if(root == null) throw new NullPointerException();
  int count = rand.nextInt(root.children + 1);
  return getRandom(root, count);
}

private int getRandom(Node curr, int count) {
  if(count == children(curr.left)) return curr.val;
  else if(count < children(curr.left)) return getRandom(curr.left, count);
  return getRandom(curr.right, count - children(curr.left) - 1);
}

private int children(Node n) {
  if(n == null) return 0;
  return n.children + 1;
}
