public static ArrayList<int[]> threeSum(int[] arr) {
  ArrayList<int[]> results = new ArrayList<int[]>();

  Arrays.sort(results);

  for(int i = 0; i < arr.length - 3; i++) {
    if(i == 0 || arr[i] > arr[i-1]) {
      int start = i + 1;
      int end = arr.length - 1;

      while(start < end) {
        if(arr[i] + arr[start] + arr[end] == 0) {
          results.add(new int[] {arr[i], arr[start], arr[end]});
        }

        if(arr[i] + arr[start] + arr[end] < 0) {
          int currentStart = start;
          while(arr[start] == arr[currentStart] && start < end) {
            start++;
          }
        } else {
          int currentEnd = end;
          while(arr[end] == arr[currentEnd] && start < end) {
            end--;
          }
        }
      }
    }
  }
  return results;
}
