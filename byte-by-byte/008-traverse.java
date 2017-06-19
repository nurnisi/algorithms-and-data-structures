private class Node {
  int value;
  Node right;
  Node left;
}

public void traverse(Node tree) {
  if(tree == null) return;
  Queue<Node> toVisit = new LinkedList<Node>();
  toVisit.add(tree);
  while(!toVisit.empty) {
    Node curr = toVisit.remove();
    System.out.println(curr.value());
    if(curr.left != null) toVisit.add(curr.left);
    if(curr.right != null) toVisit.add(curr.right);
  }
}
