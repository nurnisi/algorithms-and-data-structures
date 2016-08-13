
public class ShellSort {

	public static void sort(int[] a){
		int N = a.length;
		int h = 1;
		while(h < N/3) h = h*3 + 1;

		while(h >= 1){
			for(int i = h; i < N; i++){
				for(int j = i; j>=h && a[j]<a[j-h]; j -= h)
					swap(a, j, j-h);
			}
			h = h/3;
		}
	}

	public static void swap(int[] a, int i, int j){
		int swap = a[i];
		a[i] = a[j];
		a[j] = swap;
	}
}
