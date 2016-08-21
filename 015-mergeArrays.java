//by me
public static int[] mergeArrays(int[] arr1, int[] arr2) {
    int i = 0, j = 0;
    while(i < arr1.length && j < arr2.length) {
      if(arr1[i] == 0) {
        arr1[i] = arr2[j];
        j++;
    } else if(arr2[j] < arr1[i]) {
        int temp = arr1[i];
        arr1[i] = arr2[j];
        arr2[j] = temp;
        i++;
      } else i++;
      for(int k : arr1) System.out.print(k + " ");
      System.out.println();
    }

    return arr1;
}
