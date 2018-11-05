public static class SetOfStacks {
  int threshold, currThreshold, lastStack;
  List<Deque<Integer>> list;

  SetOfStacks(int threshold) {
    this.threshold = threshold;
    currThreshold = 0;
    list = new ArrayList<>();
    lastStack = -1;
  }

  public void push(int item) {
    if (lastStack == -1 || currThreshold == threshold) {
      Deque<Integer> stack = new LinkedList<>();
      list.add(stack);
      currThreshold = 0;
      lastStack = list.size() - 1;
    }

    Deque<Integer> stack = list.get(lastStack);
    stack.push(item);
    list.set(lastStack, stack);
    currThreshold++;
  }

  public int pop() {
    if (lastStack == -1) return Integer.MAX_VALUE;

    Deque<Integer> stack = list.get(lastStack);
    int item = stack.pop();
    currThreshold--;

    if (stack.isEmpty()) {
      lastStack--;
      currThreshold = threshold;
    }

    return item;
  }
}

// CTCI popAt()
public class SetOfStacks {
  List<Stack> stacks = new ArrayList<>();
  int capacity;

  SetOfStacks(int capacity) {
    this.capacity = capacity;
  }

  public Stack getLastStack() {
    if (stacks.isEmpty()) return null;
    return stacks.get(stacks.size() - 1);
  }

  public void push(int item) {
    Stack last = getLastStack();
    if (last != null && !last.isFull()) {
      last.push(v);
    } else {
      Stack stack = new Stack(capacity);
      stack.push(item);
      stacks.add(stack);
    }
  }

  public int pop() {
    Stack last = getLastStack();
    if (last == null) throw new EmptyStackException;
    int item = last.pop();
    if (last.size == 0) stacks.remove(stacks.size() - 1);
    return item;
  }

  public boolean isEmpty() {
    Stack last = getLastStack();
    return last == null || last.isEmpty();
  }

  public int popAt(int index) {
    return leftShift(index, true);
  }

  private int leftShift(int index, boolean removeTop) {
    Stack stack = stacks.get(index);
    int removedItem;
    if (removeTop) removedItem = stack.pop();
    else removedItem = stack.removeBottom();
    if (stack.isEmpty()) stacks.remove(index);
    else if (stacks.size() > index + 1) {
      int item = leftShift(index + 1, false);
      stack.push(item);
    }
    return removedItem;
  }
}

public class Stack {
  private int capacity;
  public Node top, bottom;
  public int size = 0;

  public Stack(int capacity) { this.capacity = capacity; }
  public boolean isFull() { return capacity == size; }

  public void join(Node above, Node below) {
    if (below != null) below.above = above;
    if (above != null) above.below = below;
  }

  public boolean push(int item) {
    if (size >= capacity) return false;
    size++;
    Node n = new Node(item);
    if (size == 1) bottom = n;
    join(n, top);
    top = n;
    return true;
  }

  public int pop() {
    Node t = top;
    top = top.below;
    size--;
    return t.value;
  }

  public boolean isEmpty() {
    return size == 0;
  }

  public int removeBottom() {
    Node b = bottom;
    bottom = bottom.above;
    if (bottom != null) bottom.below = null;
    size--;
    return b.value;
  }
}
