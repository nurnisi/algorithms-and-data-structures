//brute force - runtime O(n*m)
public static boolean contains(int[][] arr, int x) {
  if(arr.length == 0 || arr[0].length == 0) return false;

  for(int i = 0; i < arr.length; i++) {
    for(int j = 0; i < arr[0].length; i++) {
      if(arr[i][j] == x) return true;
    }
  }

  return false;
}
//binary search - runtime O(n * logm)
public static boolean contains(int[][] arr, int x) {
  if(arr.length == 0 || arr[0].length == 0) return false;

  int start, mid, end;

  for(int i = 0; i < arr.length; i++) {
    start = 0;
    end = arr[0].length;
    while(start <= end) {
      mid = start + (end - start) / 2;
      if(arr[i][mid] == x) return true;
      else if(arr[i][mid] > x) {
        start = mid++;
      } else {
        end = mid--;
      }

    }
  }
  return false;
}
//by sam - runtime O(n + m)
public static boolean contains(int[][] arr, int x) {
  if(arr.length == 0 && arr[0].length == 0) return false;

  int row = 0;
  int col = arr[0].length;

 while(row < arr.length && col >= 0) {
   if(arr[row][col] == x) return true;
   if(arr[row][col] < x) row++;
   else col--;
 }

 return false;
}
