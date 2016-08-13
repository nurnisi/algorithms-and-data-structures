
public class QueueLinkedList {
	private Node first, last;

	private class Node {
		String item;
		Node next;
	}

	private boolean isEmpty() {
		return first == null;
	}

	public void enqueue(String item) {
		Node oldLast = last;
		last.item = item;
		last.next = null;
		if(isEmpty()) first = last;
		else oldLast.next = last;
	}

	public String dequeue(){
		String item = first.item;
		first = first.next;
		if(isEmpty()) last = null;
		return item;
	}
}
