private class Node {
  List<Node> next;
}
public static List<Node> shortestPath(Node a, Node b) {
  if(a == null || b == null) return null;

  Queue<Node> toVisit = new LinkedList<Node>();
  HashMap<Node, Node> parents = new HashMap<Node, Node>();

  toVisit.add(a);
  parents.put(a, null);

  while(!toVisit.isEmpty) {
    Node curr = toVisit.remove();
    if(curr == b) break;
    for(Node n : curr.next) {
      if(!parents.containsKey(n)) {
        toVisit.add(n);
        parents.put(n, curr);
      }
    }
  }

  if(parents.get(b) == null) return null;

  List<Node> out = new LinkedList<Node>();
  Node n = b;
  while(n != null) {
    out.add(0, n);
    n = parents.get(n);
  }

  return out;
}
