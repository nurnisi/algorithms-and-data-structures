public int[] zeroSum(int[] arr) {
  HashMap<Integer, Integer> sums = new HashMap<Integer, Integer>();
  int sum = 0;

  for(int i = 0; i <= arr.length; i++) {
    Integer oldIndex = sums.get(sum);
    if(oldIndex == null && i == arr.length) {
      return null;
    } else if(oldIndex == null) {
      sums.put(sum, i);
      sum += arr[i];
    } else {
      return Arrays.copyOfRange(arr, oldIndex, i);
    }
  }

  return null;
}
