
import java.util.Random;

import edu.princeton.cs.algs4.StdRandom;

public class Nutsandbolts {
	private static int partition(int[] a, int lo, int hi, int key) {

		int i,j;
	    for(i = j = lo; j < hi; j++){
	        if(a[j] < key){
	            swap(a,i,j);
	            i++;
	        } else if (a[j] == key){
	            swap(a,j,hi);
	            j--;
	        }
	    }
	    swap(a,hi,i);
	    return i;
	}

	public static void sort(int[] a, int[] b) {
		StdRandom.shuffle(a);
		StdRandom.shuffle(b);
		sort(a, b, 0, a.length-1);
	}

	private static void sort(int[] a, int[] b, int lo, int hi) {
		if(lo >= hi) return;
		Random rn = new Random();
	    int ch = lo + rn.nextInt(hi - lo + 1);
	    int part = partition(b,lo,hi,a[ch]);
	    partition(a,lo,hi,b[part]);
	    sort(a,b,lo,part-1);
	    sort(a,b,part+1,hi);
	}

	private static void swap(int[] a, int i, int j) {
		int temp = a[i];
		a[i] = a[j];
		a[j] = temp;
	}
}
