public static int removeElement(int[] nums, int val) {
    int i = 0;
    while(i < nums.length) {
        if(nums[i] == val) {
            int j = i + 1;
            while(j < nums.length && nums[j] == val) {
                j++;
            }
            if(j >= nums.length) {
                break;
            }
            nums[i] = nums[j];
            nums[j] = val;
        }
        i++;
    }

    int counter = 0;
    while(counter < nums.length && nums[counter] != val) counter++;

    return counter;
}

//Solution
public static int removeElement(int[] nums, int val) {
    int begin = 0;
    for (int i = 0; i < nums.length; i++) {
        if(nums[i] != val) nums[begin++] = nums[i];
    }
    return begin;
}
