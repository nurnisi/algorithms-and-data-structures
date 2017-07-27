public class StackMin {
  private static class StackNode {
    private int data;
    private StackNode next;
    private int min;

    public StackNode(int data) {
      this.data = data;
    }
  }

  private StackNode top;

  public int min() {
    if (top == null) throw new EmptyStackException();
    return top.min;
  }

  public int pop() {
    if (top == null) throw new EmptyStackException();
    int data = top.data;
    top = top.next;
    return data;
  }

  public void push(int data) {
    StackNode newTop = new StackNode(data);
    newTop.next = top;

    if (top != null && top.data >= data) newTop.min = data;
    else newTop.min = top.data;

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
