
public class MinPQ {
	private int[] pq;
	private int N;

	public MinPQ(int capacity) {
		pq = new int[capacity+1];
		N = 0;
	}

	public boolean isEmpty() {
		return N == 0;
	}

	public void insert(int key) {
		pq[++N] = key;
		swim(N);
	}

	public int delMin() {
		int max = pq[1];
		swap(1, N--);
		sink(1);
		pq[N+1] = 0;
		return max;
	}

	private void swim(int k) {
		while(k > 1 && greater(k/2, k)) {
			swap(k, k/2);
			k = k/2;
		}
	}

	private void sink(int k) {
		while(2*k <= N) {
			int j = 2*k;
			if(j < N && greater(j, j+1)) j++;
			if(!greater(k, j)) break;
			swap(k, j);
			k = j;
		}
	}

	private boolean greater(int i, int j) {
		return pq[i] > pq[j];
	}

	private void swap(int i, int j) {
		int temp = pq[i];
		pq[i] = pq[j];
		pq[j] = temp;
	}
}
