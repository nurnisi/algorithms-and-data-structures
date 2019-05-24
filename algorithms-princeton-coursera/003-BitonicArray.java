
public static int BinarySearchAscending(int[] array, int key, int low, int high) {
	int lo = low;
	int hi = high;
	while(lo <= hi){
		int mid = lo + (hi-lo)/2;
		if(key < array[mid]) hi = mid-1;
		else if(key > array[mid]) lo = mid+1;
		else {
			System.out.println(mid);
			return mid;
		}
	}
	return -1;
}

public static int BinarySearchDescending(int[] array, int key, int low, int high) {
	int lo = low;
	int hi = high;
	while(lo <= hi){
		int mid = lo + (hi-lo)/2;
		if(key < array[mid]) lo = mid+1;
		else if(key > array[mid]) hi = mid-1;
		else {
			System.out.println(mid);
			return mid;
		}
	}
	return -1;
}

public static int BinarySearchForBitonicMaximum(int[] array){
	int lo = 0;
	int hi = array.length-1;
	while(lo <= hi){
		int mid = lo + (hi-lo)/2;
		if(array[mid-1] > array[mid] && array[mid] > array[mid+1]) hi = mid-1;
		else if(array[mid-1] < array[mid] && array[mid] < array[mid+1]) lo = mid+1;
		else return mid;
	}
	return -1;
}

public static void BitonicSearch(int[] array, int lo, int hi, int key){
	int mid = lo + (hi-lo)/2;
	if(key == array[mid]) System.out.println(mid);;

	if(lo <= hi){
		if(key > array[mid] && array[mid-1] > array[mid]) BitonicSearch(array, lo, mid-1, key);
		else if(key > array[mid] && array[mid-1] < array[mid]) BitonicSearch(array, mid+1, hi, key);
		else {
			BinarySearchAscending(array, key, lo, mid-1);
			BinarySearchDescending(array, key, mid+1, hi);
		}
	}
}
