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
