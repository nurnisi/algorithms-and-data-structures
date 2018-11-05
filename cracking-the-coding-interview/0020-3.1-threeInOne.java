public class FixedMultiStack {
  private int numberOfStacks = 3;
  private int stackCapacity;
  private int[] values;
  private int[] sizes;

  public FixedMultiStack(int stackSize) {
    stackCapacity = stackSize;
    values = new int[stackSize * numberOfStacks];
    size = new int[numberOfStacks];
  }

  public void push(int stackNum, int value) throws FullStackException {
    if (isFull(stackNum)) throw new FullStackException();
    sizes[stackNum]++;
    values[indexOfTop(stackNum)] = value;
  }

  public int pop(int stackNum) throws throws EmptyStackException {
    if (isEmpty(stackNum)) throw new EmptyStackException();
    int topIndex = indexOfTop(stackNum);
    int value = values[topIndex]
    values[topIndex] = 0;
    sizes[stackNum]--;
    return value;
  }

  public int peek(int stackNum) throws throws EmptyStackException {
    if (isEmpty(stackNum)) throw new EmptyStackException();
    return values[indexOfTop(stackNum)];
  }

  public boolean isFull(int stackNum) {
    return sizes[stackNum] == stackCapacity;
  }

  public boolean isEmpty(int stackNum) {
    return sizes[stackNum] == 0;
  }

  public int indexOfTop(stackNum) {
    int offset = stackNum * stackCapacity;
    int size = sizes[stackNum];
    return offset + size - 1;
  }
}

//not fixed multistack (KStack)
// Java program to demonstrate implementation of k stacks in a single
// array in time and space efficient way
static class KStack {
  int arr[];   // Array of size n to store actual content to be stored in stacks
  int top[];   // Array of size k to store indexes of top elements of stacks
  int next[];  // Array of size n to store next entry in all stacks
               // and free list
  int k, n;
  int free; // To store beginning index of free list

  //constructor to create k stacks in an array of size n
  KStack(int k1, int n1) {
    // Initialize n and k, and allocate memory for all arrays
    k = k1;
    n = n1;
    arr = new int[n];
    top = new int[k];
    next = new int[n];

    // Initialize all stacks as empty
    for (int i = 0; i < k; i++)
      top[k] = -1;

    // Initialize all spaces as free
    free = 0;
    for (int i = 0; i < n - 1; i++)
      next[i] = i + 1;

    next[n - 1] = -1; // -1 is used to indicate end of free list
  }
  // A utility function to check if there is space available
  boolean isFull() {
    return free == -1;
  }
  // To push an item in stack number 'stackNumber' where sn is from 0 to k-1
  void push(int item, int stackNumber) {
    // Overflow check
    if(isFull()) return;

    // Store index of first free slot
    int i = free;

    // Update index of free slot to index of next slot in free list
    free = next[i];

    // Update next of top and then top for stack number 'stackNumber'
    next[i] = top[stackNumber];
    top[stackNumber] = i;

    // Put the item in array
    arr[i] = item;
  }
  // To check whether stack number 'stackNumber' is empty or not
  boolean isEmpty(int stackNumber) {
    return top[stackNumber] == -1;
  }
  // To pop an from stack number 'stackNumber' where sn is from 0 to k-1
  int pop(int stackNumber) {
    // Underflow check
    if(isEmpty()) return Integer.MAX_VALUE;

    // Find index of top item in stack number 'stackNumber'
    int i = top[stackNumber];

    // Change top to store next of previous top
    top[stackNumber] = next[i];

    // Attach the previous top to the beginning of free list
    next[i] = free;
    free = i;

    // Return the previous top item
    return arr[i];
  }
}
