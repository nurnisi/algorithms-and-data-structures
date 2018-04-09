public static void moveZeroes(int[] nums) {
    int i = 0;
    while(i < nums.length) {
        if(nums[i] == 0) {
            int j = i + 1;
            while(j < nums.length && nums[j] == 0) {
                j++;
            }
            if(j >= nums.length) break;
            nums[i] = nums[j];
            nums[j] = 0;
        }
        i++;
    }
}

//O(N)
public static void moveZeroes(int[] nums) {
    int insertPosition = 0;

    for (int i = 0; i < nums.length; i++) {
        if(nums[i] != 0) nums[insertPosition++] = nums[i];
    }

    while(insertPosition < nums.length) nums[insertPosition++] = 0;

    for(int j : nums) System.out.println(j);
}
