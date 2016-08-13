
public class QueueArray {
	private String[] s;
	private int head = 0, tail = 0;

	public QueueArray() {
		s = new String[1];
	}

	private boolean isEmpty() {
		return tail == 0;
	}

	public void enqueue(String item) {
		if(tail==s.length) resize((tail-head)*2);
		s[tail++] = item;
	}

	private void resize(int capacity) {
		String[] copy = new String[capacity];
		int j = 0;
		while(head < tail){
			copy[j++] = s[head++];
		}
		s = copy;
		head = 0;
		tail = j;
		System.out.println(s.length);
	}

	public String dequeue(){
		String item = s[head];
		s[head++] = null;
		int N = tail-head;
		if(N>0 && N==s.length/4) resize(s.length/2);
		return item;
	}
}
