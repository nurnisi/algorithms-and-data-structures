public class Stack {
  private static class StackNode {
    private int data;
    private StackNode next;

    public StackNode(int data) {
      this.data = data;
    }
  }

  private StackNode top;

  public int pop() {
    if (top == null) throw new EmptyStackException();
    int data = top.data;
    top = top.next;
    return data;
  }

  public void push(int data) {
    StackNode newTop = new StackNode(data);
    newTop.next = top;
    top = newTop;
  }

  public int peek() {
    if (top == null) throw new EmptyStackException();
    return top.data;
  }

  public boolean isEmpty() {
    return top == null;
  }
}
