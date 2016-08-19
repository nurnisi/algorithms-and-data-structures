//by me
public class Stack {
  private class Node {
    int value;
    Node next;
  }

  private Node first = null;

  public void push(int value) {
    Node oldFirst = first;
    first.value = value;
    first.next = oldFirst;
  }

  public int pop() {
    if(first == null) throw new NullPointerException();

    int value = first.value;
    first = first.next;

     return value;
  }

  public boolean palindrome(Node linkedList) {
    Stack stack = new Stack();
    Node curr = linkedList;
    int size = 0;
    while(curr != null) {
      stack.push(curr.value);
      curr = curr.next;
      size++;
    }
    size /= 2;
    while(size != 0) {
      if(linkedList.value != stack.pop()) return false;
      linkedList = linkedList.next;
      size--;
    }
    return true;
  }
}
//by sam
 public boolean palindrome(Node head) {
   Stack<Integer> stack = new Stack<Integer>();
   Node curr = head;
   Node runner = head;

   while(runner != null && runner.next != null) {
     stack.push(curr.value);
     curr = curr.next;
     runner = runner.next.next;
   }

   if(runner != null) curr = curr.next;

   while(curr != null) {
     if(curr.value != stack.pop()) return false;
     curr = curr.next;
   }

   return true;
 }
