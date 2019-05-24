
public class DutchNationalFlagWithNumbers {
	public static void sort(int[] a){
		int N = a.length;
		assert N > 0;
		int runner = 0;
		int r = 0;
		int b = N-1;

		while(runner <= b){
			if(a[runner] < 1) {
				swap(a,runner,r);
				runner++;
				r++;
			}
			else if(a[runner] > 1) {
				swap(a,runner,b);
				b--;
			}
			else runner++;
		}
	}

	private static void swap(int[] a, int i, int j){
		int temp = a[i];
		a[i] = a[j];
		a[j] = temp;
	}
}
