public class Queue {
  private class QueueNode() {
    int data;
    QueueNode next;

    public QueueNode(int data) {
      this.data = data;
    }
  }

  QueueNode first;
  QueueNode last;

  public void add(int data) {
    QueueNode node = new QueueNode(data);
    if (last != null) last.next = node;
    last = node;
    if (first == null) first = last;
  }

  public int remove() {
    if (first == null) throw new NoSuchElementException();
    int data = first.data;
    first = first.next;
    if (first == null) last = null;
    return data;
  }

  public int peek() {
    if (first == null) throw new NoSuchElementException();
    return first.data;
  }

  public boolean isEmpty() {
    return first == null;
  }
}
