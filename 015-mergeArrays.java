//by me doesn't work in case:
//    int[] a = {4,5,6,0,0,0};
//    int[] b = {1,2,3};
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
//by sam
public void mergeArrays(int[] a, int[] b) {
  if(b.length > a.length) throw new IllegalArgumentsException();

  int aIndex = a.legnth - b.length - 1;
  int bIndex = b.length - 1;
  int mergeIndex = a.length - 1;

  while(aIndex >= 0 && bIndex >= 0) {
    if(a[aIndex] > b[bIndex]) {
      a[mergeIndex--] = a[aIndex--];
    } else {
      a[mergeIndex--] = b[bIndex--];
    }
  }

  while(bIndex >= 0) {
    a[mergeIndex--] = b[bIndex--];
  }
}
