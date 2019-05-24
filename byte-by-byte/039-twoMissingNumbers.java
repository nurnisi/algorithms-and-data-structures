//determine the single number that is missing
public static int oneMissing(int[] arr) {
  totalXor = 0;
  arrXor = 0;

  for(int i = 1; i <= arr.length + 1; i++) totalXor ^= i;
  for(int i : arr) arrXor ^= i;

  return totalXor ^ arrXor;
}

//determine two numbers that are missing
public static int[] twoMissing(int[] arr) {
  int size = arr.length + 2;
  long totalSum = size * (size + 1) / 2;
  long arrSum = 0;

  for(int i : arr) arrSum += i;

  int pivot = (int) ((totalSum + arrSum) / 2);

  int totalLeftXor = 0;
  int totalRightXor = 0;
  int arrLeftXor = 0;
  int arrRightXor = 0;

  for(int i = 1; i <= pivot; i++) totalLeftXor ^= i;
  for(int i = pivot + 1; i <= size; i++) totalRightXor ^= i;
  for(int i : arr) {
    if(i <= pivot) arrLeftXor ^= i;
    else arrRightXor ^= i;
  }

  return new int[]{totalLeftXor ^ arrLeftXor, totalRightXor ^ arrRightXor};
}
