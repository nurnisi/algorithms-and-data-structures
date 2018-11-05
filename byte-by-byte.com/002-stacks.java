public class stacks {

  private int[] s;
  private int N = 0;

  public stacks() {
    s = new int[1];
  }

  public void push(int number) {
    if(N == s.length) resize(s.length * 2);
    s[N++] = number;
  }

  public void resize(int capacity) {
    int[] copy = new int[capacity];
    for(int i = 0; i < N; i++) copy[i] = s[i];
    s = copy;
  }

  public int pop() {
    int number = s[--N];
    s[N] = null;
    if(N > 0 && N == s.length/4) resize(s.length/2);
    return number;
  }

}
