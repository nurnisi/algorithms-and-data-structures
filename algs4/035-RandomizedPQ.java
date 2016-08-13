
import edu.princeton.cs.algs4.StdRandom;

public class RandomizedPQ {
	private static int[] pq;
	private int N;

	public RandomizedPQ(int capacity) {
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

	public int delRandom() {
		int r = StdRandom.uniform(1,N);
		int rand = pq[r];
		swap(r, N--);
		if(less(r/2, r)) swim(r);
		else if(less(r, r/2) || less(r, r/2+1)) sink(r);
		pq[N+1] = 0;
		return rand;
	}

	public int sample() {
		return pq[StdRandom.uniform(1,N)];
	}

	private void swim(int k) {
		while(k > 1 && less(k/2, k)) {
			swap(k, k/2);
			k = k/2;
		}
	}

	private void sink(int k) {
		while(2*k <= N) {
			int j = 2*k;
			if(j < N && less(j, j+1)) j++;
			if(!less(k, j)) break;
			swap(k, j);
			k = j;
		}
	}

	private boolean less(int i, int j) {
		return pq[i] < pq[j];
	}

	private void swap(int i, int j) {
		int temp = pq[i];
		pq[i] = pq[j];
		pq[j] = temp;
	}


	public static void print() {
		for(int i = 0; i < pq.length; i++)
			System.out.print(pq[i] + " ");
		System.out.println();
	}
}
