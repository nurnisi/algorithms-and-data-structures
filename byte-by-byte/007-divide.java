divide(1 -> 2 -> 3 -> 4)
divide(1 -> 2 -> 3 -> 4 -> 5)

public class LinkedList {

	private class Node {
		Node next;
		int data;
	}

	private Node first = null;

	public Node[] divide(Node first) {
		if(first == null) return null;

		Node head = first, tail = first.next;

		while(tail != null || tail.next != null) {
			head = head.next;
			tail = tail.next.next;
		}

		second = head.next;
		head.next = null;

		Node[] result = new Node[2]();
		result.push(first);
		result.push(second );

		return result;

	}

}
