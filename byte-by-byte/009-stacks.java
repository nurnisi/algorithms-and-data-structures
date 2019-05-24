public class Stacks {

  private int[] topOfStack;
  private int[] stackData;
  private int[] nextIndex;

  private int nextAvailable = 0;

  public Stacks(int numStack, int capacity) {
    topOfStack = new int[numStack];
    for(int i = 0; i < topOfStack.length; i++) topOfStack[i] = -1;

    stackData = new int[capacity];

    nextIndex = new int[capacity];
    for(int i = 0; i < nextIndex.length - 1; i++) nextIndex[i] = i+1;
    nextIndex[nextIndex.length - 1] = -1;
  }

  public void push(int stack, int value) {
    if(stack < 0 || stack >= topOfStack.length) throw new IndexOutOfBoundsException();

    if(nextAvailable < 0) return;

    int currIndex = nextAvailable;
    nextAvailable = nextIndex[currIndex];
    nextIndex[currIndex] = topOfStack[currIndex];
    topOfStack[currIndex] = currIndex;
    stackData[currIndex] = value;
  }

  public int pop(int stack) {
    if(stack < 0 || stack >= topOfStack.length || topOfStack[stack] < 0)
      throw new IndexOutOfBoundsException();

    int currIndex = topOfStack[stack];
    int value = stackData[currIndex];
    topOfStack[stack] = nextIndex[currIndex];
    nextIndex[currIndex] = nextAvailable;
    nextAvailable = currIndex;

    return value;
  }

}
