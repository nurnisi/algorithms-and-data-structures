
public class MedianMerge{
	public static int getMedian(int[] a, int[] b) {
		int i = 0, j = 0;
		int first = 0, second = 0;
		for(int k = 0; k <= a.length; k++) {
			if(b[j] < a[i]) {
				second = first;
				first = b[j];
				j++;
			}
			else {
				second = first;
				first = a[i];
				i++;
			}
		}
		return (first+second)/2;
	}
}
