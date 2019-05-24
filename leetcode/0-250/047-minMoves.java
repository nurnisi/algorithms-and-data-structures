public static int minMoves(int[] nums) {
    Arrays.sort(nums);
    int min = 0, max = nums.length - 1, moves = 0;
    while(nums[min] != nums[max]) {
        moves += nums[max] - nums[min];
        max--;
    }
    return moves;
}
