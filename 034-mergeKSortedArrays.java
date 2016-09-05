private class QueueNode implements Comparable<QueueNode> {
  int array, index, value;

  public QueueNode(int array, int index, int value) {
    this.array = array;
    this.index = index;
    this.value = value;
  }

  public int compareTo(QueueNode n) {
    if(value > n.value) return 1;
    if(value < n.value) return -1;
    return 0;
  }
}

public static int[] merge(int[][] arrays) {
  PriorityQueue<QueueNode> pq = new PriorityQueue<QueueNode>();

  int size = 0;
  for(int i = 0; i < arrays.length; i++) {
    size += arrays[i].length;
    if(arrays[i].length > 0) {
      pq.add(new QueueNode(i, 0, arrays[i][0]));
    }
  }

  int[] result = new int[size];
  for(int i = 0; !pq.isEmpty(); i++) {
    QueueNode n = pq.poll();
    result[i] = n.value;
    int newIndex = n.index + 1;
    if(newIndex < arrays[n.array].length) {
      pq.add(new QueueNode(n.array, newIndex, arrays[n.array][newIndex]));
    }
  }

  return result;
}
