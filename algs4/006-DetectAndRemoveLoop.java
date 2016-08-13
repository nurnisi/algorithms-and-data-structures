
public boolean detectLoop(){
	Node tortoise = first;
	Node hare = first;
	while(hare != null && hare.next != null){
		tortoise = tortoise.next;
		hare = hare.next.next;
		if(tortoise == hare) {
			System.out.println(tortoise.item + " " + hare.item);
			removeLoop(hare);
			return true;
		}
	}
	return false;
}

private void removeLoop(Node node){
	Node ptr1 = first;
	Node ptr2 = node;
	while(ptr1 != ptr2){
		ptr1 = ptr1.next;
		ptr2 = ptr2.next;
	}
	System.out.println("Loop start - " + ptr2.item);
}
