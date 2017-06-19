public class stackLinkedList {

  private class Node {
    int value;
    Node next;
    Node oldMax;
  }

  private Node first = null;
  private Node max = null;

  public void push(int n) {
    Node oldFirst = first;
    first = new Node();
    first.value = n;
    first.next = oldFirst;

    if(max == null || first.value > max.value) {
      first.oldMax = max;
      max = first;
    }
  }

  public int pop(){
    if(first == null) throw new NullPointerException;

    if(first.oldMax != null) max = first.oldMax;

    int value = first.value;
    first = first.next;
    return value;
  }

  public int max() {
    if(max == null) throw new NullPointerException;
    return max.value;
  }

}
