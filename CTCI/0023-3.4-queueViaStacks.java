//constant pop() time
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

//constant push() time
public class MyQueue {
  Stack temp, main;

  public MyQueue() {
    temp = new Stack();
    main = new Stack();
  }

  public void push(int item) {
    main.push(item);
  }

  public int pop() {
    if (main.isEmpty) throw new EmptyQueueException;
    int item;
    while (!main.isEmpty()) {
      item = main.pop();
      if (!main.isEmpty()) temp.push(item);
    }
    while (!temp.isEmpty()) main.push(temp.pop());
    return item;
  }
}

public class Stack { ... }
