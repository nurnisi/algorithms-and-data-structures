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
//by sam
public class Stack {
  private Queue<Integer> primary = new LinkedList<Integer>();
  private Queue<Integer> secondary = new LinkedList<Integer>();

  public Stack() {}

  public void push(int x) {
    secondary.add(x);
    while(!primary.isEmpty()) {
      secondary.add(primary.remove);
    }

    Queue<Integer> temp = primary;
    primary = secondary;
    secondary = temp;
  }

  public int pop() {
    if(primary.isEmpty()) throw new NullPointerException();
    return primary.remove();
  }
}
//another solution
public class Stack {
  private Queue<Integer> primary = new LinkedList<Integer>();
  private Queue<Integer> secondary = new LinkedList<Integer>();

  public Stack() {}

  public void push(int x) {
    primary.add(x);
  }

  public int pop() {
    if(primary.isEmpty()) throw new NullPointerException();
    Integer value = null;
    while(!primary.isEmpty) {
      value = primary.remove();
      if(!primary.isEmpty()) secondary.add(value);
    }

    Queue<Integer> temp = primary;
    primary = secondary;
    secondary = temp;

    return value.intValue();
  }
}
