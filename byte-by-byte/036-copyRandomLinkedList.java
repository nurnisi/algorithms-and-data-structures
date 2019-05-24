private class Node {
  Node next;
  Node random;
}
//without extra space
public static Node copyWithoutExtraSpace(Node n) {
  if(n == null) return n;

  Node nCurr = n;
  while(nCurr != null) {
    Node temp = new Node();
    temp.next = nCurr.next;
    nCurr.next = temp;
    nCurr = nCurr.next;
  }

  nCurr = n;
  while(nCurr != null) {
    nCurr.next.random = nCurr.random.next;
    nCurr = nCurr.next.next;
  }

  Node copy = n.next;
  nCurr = n;
  while(nCurr.next != null) {
    Node temp = nCurr.next;
    nCurr.next = nCurr.next.next;
    nCurr = temp;
  }

  return copy;
}

//with extra space
public static Node copyWithExtraSpace(Node n) {
  if(n == null) return n;

  HashMap<Node, Node> mapping = new HashMap<Node, Node>();
  Node copy = new Node();
  Node nCurr = n, copyCurr = copy;

  while(nCurr != null) {
    mapping.put(nCurr, copyCurr);
    copyCurr.next = new Node();
    nCurr = nCurr.next;
    copyCurr = copyCurr.next;
  }

  nCurr = n;
  copyCurr = copy;

  while(nCurr != null) {
    copyCurr.random = mapping.get(nCurr.random);
    copyCurr = copyCurr.next;
    nCurr = nCurr.next;
  }

  return copy;
}
