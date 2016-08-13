
public class LinkedListWithRandom {
	public Node first = null;

	public class Node {
		String item;
		Node next;
		Node random;
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

	public LinkedListWithRandom copy(){

		Node ptr = this.first;
		Node copy;
		while(ptr != null){
			copy = new Node();
			copy.item = ptr.item;
			copy.next = ptr.next;
			copy.random = ptr.random;
			ptr.next = copy;
			ptr = ptr.next.next;
		}
		ptr = new Node();
		ptr = this.first;
		LinkedListWithRandom c = new LinkedListWithRandom();
		c.first = this.first.next;
		while(ptr != null){
			copy = new Node();
			copy.item = ptr.next.item;
			copy.next = ptr.next.next;
			copy.random = ptr.next.random;
			ptr.next = ptr.next.next;
			if(copy.next != null) copy.next = copy.next.next;
			ptr = ptr.next;
		}
		return c;
	}
}
