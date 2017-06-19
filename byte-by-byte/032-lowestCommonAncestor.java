public class Node {
  int value;
  Node left;
  Node right;
}

public static Node lowestCommonAncestor(Node tree, Node n1, Node n2) {
  if(n1.value == n2.value) return n1;

  Stack<Node> pathNo1 = pathTo(tree, n1);
  Stack<Node> pathNo2 = pathTo(tree, n2);

  if(pathNo1 == null || pathNo2 == null) return null;

  Node prev = null;
  while(!pathNo1.isEmpty() && !pathNo2.isEmpty()) {
    Node s = pathNo1.pop();
    Node t = pathNo2.pop();
    if(s.value == t.value) prev = s;
    else break;
  }

  return prev;
}

private static Stack<Nodes> pathTo(Node tree, Node n) {
  if(tree == null) return null;
  if(tree.value == n.value) {
    Stack<Node> s = new Stack<Node>();
    s.push(tree);
    return s;
  }

  Stack<Node> left = pathTo(tree.left, n);
  Stack<Node> right = pathTo(tree.right, n);

  if(left != null) {
    left.push(tree);
    return left;
  }

  if(right != null) {
    right.push(tree);
    return right;
  }

  return null;
}

//time complexity = O(n)
//space complexity = O(n)
