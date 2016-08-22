//by me
public class stackViaQueue {
  private int N = 0;
  Queue<int> stack = new LinkedList<Int>();

  public void push(int value) {
    stack.add(value);
    N++;
  }

  public int pop() {
    int i = --N;
    while(i > 0) {
      int value = stack.remove();
      stack.add(value);
      i--;
    }
    return stack.remove;
  }
}
