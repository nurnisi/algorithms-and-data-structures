public static int removeDuplicates(int[] nums) {
    if(nums.length == 0 || nums.length == 1) return nums.length;

    int begin = 1;
    int number = nums[0];
    for (int i = 1; i < nums.length; i++) {
        if (nums[i] != number) {
            nums[begin] = nums[i];
            number = nums[begin++];
        }
    }

    return begin;
}
