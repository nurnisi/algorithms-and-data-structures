
import java.util.Iterator;
import java.util.NoSuchElementException;

public class Deque<Item> implements Iterable<Item> {

	private Node first, last;
	private int N;

	private class Node {
		Item item;
		Node next;
		Node previous;
	}

	public Deque() {
		// construct an empty dequeue
		first = null;
		last = null;
		N = 0;
	}
	public boolean isEmpty() {
		// is the dequeue empty?
		return N == 0;
	}

	public int size() {
		// return the number of items on the dequeue
		return N;
	}

	public void addFirst(Item item) {
		// add the item to the front
		if(item == null) throw new NullPointerException();
		Node oldFirst = first;
		first.item = item;
		first.next = oldFirst;
		if(isEmpty()) last = first;
		else oldFirst.previous = first;
		N++;
	}

	public void addLast(Item item) {
		// add the item to the end
		if(item == null) throw new NullPointerException();
		Node oldLast = last;
		last.item = item;
		last.previous = oldLast;
		last.next = null;
		if(isEmpty()) first = last;
		else oldLast.next = last;
		N++;
	}

	public Item removeFirst() {
		// remove and return the item from the front
		if(isEmpty()) throw new NoSuchElementException();
		Item item = first.item;
		first = first.next;
		N--;
		if(isEmpty()) last = null;
		else first.previous = null;
		return item;
	}

	public Item removeLast() {
		// remove and return the item from the end
		if(isEmpty()) throw new NoSuchElementException();
		Item item = last.item;
		last = last.previous;
		N--;
		if(isEmpty()) first = null;
		else last.next = null;
		return item;
	}

	public Iterator<Item> iterator() {
		return new DequeIterator();
		// return an iterator over items in order from front to end
	}

	private class DequeIterator implements Iterator<Item> {

		private Node current = first;

		@Override
		public boolean hasNext() {
			return current != null;
		}

		@Override
		public Item next() {
			if(!hasNext()) throw new NoSuchElementException();
			Item item = current.item;
			current = current.next;
			return item;
		}

	}

	public static void main(String[] args) {
		// unit testing
	}
}
