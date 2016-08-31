//by me
public static Queue<Integer> deleteDuplicates(Queue<Integer> queue) {
  if(queue.isEmpty()) return queue;

  Queue<Integer> temp = new LinkedList<Integer>();
  Set<Integer> queueElements = new HashSet<Integer>();

  while(!queue.isEmpty()) {
    int item = queue.remove();
    if(!queueElements.contains(item)) {
      temp.add(item);
      queueElements.add(item);
    }
  }

  return temp;
}
