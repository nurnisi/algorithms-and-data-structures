public static String[] findRelativeRanks(int[] nums) {
    Map<Integer, Integer> map = new HashMap<>();
    int length = nums.length;
    for (int i = 0; i < length; i++) {
        map.put(nums[i], i);
    }

    int[] temp = nums.clone();
    Arrays.sort(temp);

    String[] res = new String[length];
    for (int i = 0; i < length; i++) {
        String item = Integer.toString(length - i);
        if(i == length - 1) item = "Gold Medal";
        else if(i == length - 2) item = "Silver Medal";
        else if(i == length - 3) item = "Bronze Medal";
        int index = map.get(temp[i]);
        res[index] = item;
    }

    return res;
}

//sorting 2d Arrays
//arr = {10, 3, 8}
//create array as below
//{10, 0}
//{3, 1}
//{8, 2}
int[][] arr = new int[nums.lenth][2];
for (int i = 0; i < nums.length; i++) {
  arr[i][0] = nums[i]; //number
  arr[i][1] = i;       //index
}

Arrays.sort(pair, (a, b) -> (b[0] - a[0]));
//result
//{10, 0}
//{8, 2}
//{3, 1}
