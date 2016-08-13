
public class MergeWithSmallerAux {

	public static void sort(int[] a) {
		assert a.length%2 == 0;

		int N = a.length;
		int[] aux = new int[N/2];
		for(int i = 0; i < N/2; i++)
			aux[i] = a[i];

		int i = 0;
		int mid = (N-1)/2;
		int j = mid+1;

		for(int k = 0; k < N; k++) {
			if(i > mid) {
				a[k] = a[j++];
			}
			else if(j > N-1) {
				a[k] = aux[i++];
			}
			else if(aux[i] < a[j]) {
				a[k] = aux[i++];
			}
			else {
				a[k] = a[j++];
			}
		}
	}

}
