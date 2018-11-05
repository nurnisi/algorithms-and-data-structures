public Stack<Integer> sort(Stack<Integer> stack) {
  if(stack == null || stack.isEmpty()) return stack;

  Stack<Integer> newStack = new Stack<Integer>();
  newStack.push(stack.pop());

  while(!stack.isEmpty()) {
    int temp = stack.pop().intValue();
    while(!newStack.isEmpty() && temp > stack.peek().intValue()) {
      stack.push(newStack.pop());
    }
    newStack.push(temp);
  }

  return newStack;
}
