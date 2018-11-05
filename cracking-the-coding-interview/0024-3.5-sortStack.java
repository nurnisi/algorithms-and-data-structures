public static Stack sortStack(Stack stack) {
  Stack temp = new Stack();
  int item, counter = 0;
  while (!stack.isEmpty()) {
    item = stack.pop();
    while (!temp.isEmpty() && item > temp.peek()) {
      stack.push(temp.pop());
      counter++;
    }
    temp.push(item);
    while (counter > 0) {
      temp.push(stack.pop());
      counter--;
    }
  }
  return temp;
}

//CTCI
public static Stack sortStack(Stack stack) {
  Stack temp = new Stack();
  while (!stack.isEmpty()) {
    int item = stack.pop();
    while (!temp.isEmpty() && item > temp.peek()) stack.push(temp.pop());
    temp.push(item);
  }
  return temp;
}
