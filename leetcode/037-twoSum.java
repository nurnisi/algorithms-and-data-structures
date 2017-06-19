public static  int[] twoSum(int[] numbers, int target) {
    Map<Integer, Integer> map = new HashMap<>();

    int[] res = new int[2];
    for (int j = 0; j < numbers.length; j++) {
        if(map.get(target - numbers[j]) != null) {
            res[0] = map.get(target - numbers[j]) + 1;
            res[1] = j + 1;
            break;
        }
        map.put(numbers[j], j);
    }
    return res;
}
