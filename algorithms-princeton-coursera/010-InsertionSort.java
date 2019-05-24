
public class InsertionSort {

	public static void sort(int[] a){
		for(int i = 0; i < a.length; i++){
			for(int j = i; j > 0; j--)
				if(a[j] < a[j-1]) swap(a, j, j-1);
		}
	}

	public static void swap(int[] a, int i, int j){
		int swap = a[i];
		a[i] = a[j];
		a[j] = swap;
	}

}
