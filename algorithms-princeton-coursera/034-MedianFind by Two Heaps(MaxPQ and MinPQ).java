
public class Median {
	private static int[] max;
	private static int[] min;
	private static int N;
	private static int M;

	public Median() {
		max = new int[11];
		min = new int[11];
		N = 0;
		M = 0;
	}

	public void insert(int key) {
		if(key < max[N]) {
			max[++N] = key;
			swimMax(N);
		} else if(key > min[M]) {
			min[++M] = key;
			swimMin(M);
		}
		if(N-M > 1) balanceMax();
		else if(M-N > 1) balanceMin();
	}

	private void balanceMax() {
		int key = max[1];
		swap(max, 1, N--);
		sinkMax(1);
		max[N+1] = 0;
		min[++M] = key;
		swimMin(M);
	}

	private void balanceMin() {
		int key = min[1];
		swap(min, 1, M--);
		sinkMin(1);
		min[M+1] = 0;
		max[++N] = key;
		swimMax(N);
	}

	public double delMedian() {
		double median;
		if(N > M) {
			median = max[1];
			swap(max, 1, N--);
			sinkMax(1);
			max[N+1] = 0;
		}
		else if(N < M) {
			median = min[1];
			swap(min, 1, M--);
			sinkMin(1);
			min[M+1] = 0;
		}
		else {
			median = (max[1]+min[1]);
			median = median/2.0;

			swap(max, 1, N--);
			sinkMax(1);
			max[N+1] = 0;

			swap(min, 1, M--);
			sinkMin(1);
			min[M+1] = 0;
		}
		if(N-M > 1) balanceMax();
		else if(M-N > 1) balanceMin();
		return median;
	}

	private void swimMax(int k) {
		while(k > 1 && less(k/2, k)) {
			swap(max, k, k/2);
			k = k/2;
		}
	}

	private void sinkMax(int k) {
		while(2*k <= N) {
			int j = 2*k;
			if(j < N && less(j, j+1)) j++;
			if(!less(k, j)) break;
			swap(max, k, j);
			k = j;
		}
	}

	private void swimMin(int k) {
		while(k > 1 && greater(k/2, k)) {
			swap(min, k, k/2);
			k = k/2;
		}
	}

	private void sinkMin(int k) {
		while(2*k <= N) {
			int j = 2*k;
			if(j < N && greater(j, j+1)) j++;
			if(!greater(k, j)) break;
			swap(min, k, j);
			k = j;
		}
	}

	private boolean less(int i, int j) {
		return max[i] < max[j];
	}

	private boolean greater(int i, int j) {
		return min[i] > min[j];
	}

	private void swap(int[] arr, int i, int j) {
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}

	public static void print() {
		for(int i = 0; i < max.length; i++)
			System.out.print(max[i] + " ");
		System.out.println();
		for(int i = 0; i < min.length; i++)
			System.out.print(min[i] + " ");
	}

	public static void printnm() {
			System.out.print(N + " " + M);
	}
}
