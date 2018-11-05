
public class StackLinkedList {

	public Node first = null;

	public class Node {
		String item;
		Node next;
	}

	public boolean isEmpty(){
		return first == null;
	}

	public void push(String item){
		Node oldFirst = first;
		first = new Node();
		first.item = item;
		first.next = oldFirst;
	}

	public String pop(){
		String item = first.item;
		first = first.next;
		return item;
	}
}
