public class MyQueue {
  Stack temp, main;

  public MyQueue() {
    temp = new Stack();
    main = new Stack();
  }

  public void push(int item) {
    while (!main.isEmpty()) temp.push(main.pop());
    main.push(item);
    while (!temp.isEmpty()) main.push(temp.pop());
  }

  public int pop() {
    return main.pop();
  }
}

public class Stack { ... }
