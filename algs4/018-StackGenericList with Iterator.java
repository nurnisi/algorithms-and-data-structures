
import java.util.Iterator;

public class StackGenericList<Item> implements Iterable<Item> {
	public Node first = null;

	public class Node {
		Item item;
		Node next;
	}

	public boolean isEmpty(){
		return first == null;
	}

	public void push(Item item){
		Node oldFirst = first;
		first = new Node();
		first.item = item;
		first.next = oldFirst;
	}

	public Item pop(){
		Item item = first.item;
		first = first.next;
		return item;
	}

	@Override
	public Iterator<Item> iterator() {
		return new ListIterator();
	}

	private class ListIterator implements Iterator<Item> {

		private Node current = first;

		@Override
		public boolean hasNext() {
			return current != null;
		}

		@Override
		public Item next() {
			Item item = current.item;
			current = current.next;
			return item;
		}

	}
}
