public static int consecutive(int[] nums) {
    Arrays.sort(nums);

    int seq = 1, runner = 1;
    for (int i = 0; i < nums.length - 1; i++) {
        if (nums[i] + 1 == nums[i + 1]) {
            runner++;
            if(seq < runner) seq = runner;
        }
        else runner = 1;
    }
    return seq;
}

//HashSet
public static int consecutive(int[] nums) {
    HashSet<Integer> set = new HashSet<>();
    for(int i : nums) set.add(i);

    int maxLength = 1;
    for(int j : nums) {
      if(set.contains(j - 1)) continue;
      int length = 1;

      while(set.contains(++j)) length++;
      maxLength = Math.max(maxLength, length);
    }

    return maxLength;
}
