
public class Heap {
	public static void sort(int[] a) {
		int N = a.length;
		for(int k  = N/2; k >= 1; k--)
			sink(a, k, N);
		while(N > 1) {
			swap(a, 1, N);
			sink(a, 1, --N);
		}
	}

	private static void sink(int[] a, int k, int N) {
		while(2*k <= N) {
			int j = 2*k;
			if(j < N && less(a, j, j+1)) j++;
			if(!less(a, k, j)) break;
			swap(a, k, j);
			k = j;
		}
	}

	private static boolean less(int[] a, int i, int j) {
		return a[i-1] < a[j-1];
	}

	private static void swap(int[] a, int i, int j) {
		int temp = a[i-1];
		a[i-1] = a[j-1];
		a[j-1] = temp;
	}
}
