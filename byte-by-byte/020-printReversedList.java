public class Node {
  int value;
  Node next = null;
}

//by stack
public static void printReversedList(Node list) {
  Stack<Integer> stack = new Stack<Integer>();
  Node curr = list;

  while(curr != null) {
    stack.push(curr.value);
    curr = curr.next;
  }

  while(!stack.empty()) {
    System.out.println(stack.pop());
  }
}
//by recursion
public static void printReversedList(Node list) {
  Node curr = list;
  if(curr == null) return;
  printReversedList(Node curr.next);
  System.out.println(curr.value);
}
