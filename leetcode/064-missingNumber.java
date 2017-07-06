public static int missingNumber(int[] nums) {
    int sum1 = nums.length * (nums.length + 1) / 2, sum2 = 0;
    for (int i = 0; i < nums.length; i++) {
        sum2 += nums[i];
    }
    return sum1 - sum2;
}

//bit manipulation
public int missingNumber(int[] nums) {
    int xor = 0, i = 0;
    for (i = 0; i < nums.length; i++) {
        xor = xor ^ i ^ nums[i];
    }
    return xor ^ i;
}
