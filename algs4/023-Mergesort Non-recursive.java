
public class MergesortBottomup {

	private static void merge(int[] a, int[] aux, int lo, int mid, int hi) {
		for(int k = 0; k <= hi; k++)
			aux[k] = a[k];

		int i = lo, j = mid+1;
		for(int k = lo; k <= hi; k++) {
			if(i > mid) a[k] = aux[j++];
			else if(j > hi) a[k] = aux[i++];
			else if(aux[j] < aux[i]) a[k] = aux[j++];
			else a[k] = aux[i++];
		}
	}

	public static void sort(int[] a) {
		int N = a.length;
		int[] aux = new int[N];
		for(int sz = 1; sz < N; sz+=sz)
			for(int lo = 0; lo < N-sz; lo += sz+sz)
				merge(a, aux,lo, lo+sz-1, Math.min(lo+sz+sz-1, N-1));
	}
}
