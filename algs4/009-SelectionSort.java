
public class SelectionSort{

	public static void sort(int[] a){
		int N = a.length;
		for(int i = 0; i < N; i++){
			int min = i;
			for(int j = i+1; j < N; j++){
				if(a[j] < a[min]) min = j;
			}
			swap(a, i, min);
		}
	}

	public static void swap(int[] a, int i, int j){
		int swap = a[i];
		a[i] = a[j];
		a[j] = swap;
	}

	public static boolean isSorted(int[] a){
		for(int i = 1; i < a.length; i++)
			if(a[i] < a[i-1]) return false;
		return true;
	}

}
