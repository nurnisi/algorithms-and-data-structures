public static void reverse(Stack<Integer> stack) {
  if(stack.isEmpty()) return;

  int temp = stack.pop();
  reverse(stack);
  insertAtBottom(stack, temp);
}

private static void insertAtBottom(Stack<Integer> stack, int x) {
  if(stack.isEmpty()) {
    stack.push(x);
  }

  int temp = stack.pop();
  insertAtBottom(stack, x);
  stack.push(temp);
}

/*
time complexity:
insertAtBottom = O(n)
reverse = O(n) * O(n) = O(n^2)

space complexity:
insertAtBottom = O(n)
reverse = O(n) + O(n) = O(2n) = O(n)
*/
