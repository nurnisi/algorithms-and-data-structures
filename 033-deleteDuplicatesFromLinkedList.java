//by Sam using HashSet
//time complexity: O(n)
//space complexity: O(n)
public class Node {
  int value;
  Node next;
}

public static void deleteDuplicates(Node n) {
  if(n == null) return;
  HashSet<Integer> set = new HashSet<Integer>();
  Node prev = null;

  while(n != null) {
    if(set.contains(n.val)) {
      prev.next = n.next;
    } else {
      set.add(n.val);
      prev = n;
    }
    n = n.next;
  }
  prev.next = null;
}

//by Sam without using HashSet
//time complexity: O(n^2)
//space complexity: O(1)
public static void deleteDuplicates(Node n) {
  while(n != null) {
    Node curr = n;
    while(curr.next != null) {
      if(curr.next.value == n.value) {
        curr.next = curr.next.next;
      } else {
        curr = curr.next;
      }
    }
    n = n.next;
  }
}

//by me from Queue
public static Queue<Integer> deleteDuplicates(Queue<Integer> queue) {
  if(queue.isEmpty()) return queue;

  Queue<Integer> temp = new LinkedList<Integer>();
  Set<Integer> queueElements = new HashSet<Integer>();

  while(!queue.isEmpty()) {
    int item = queue.remove();
    if(!queueElements.contains(item)) {
      temp.add(item);
      queueElements.add(item);
    }
  }

  return temp;
}
