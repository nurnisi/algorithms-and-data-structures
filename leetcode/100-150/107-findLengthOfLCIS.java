import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(findLengthOfLCIS(new int[]{1,2,5,8,0}));
    }

    public static int findLengthOfLCIS(int[] nums) {
        if (nums.length == 0) return 0;
        int max = 1, count = 1;
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i+1] - nums[i] > 0) count++;
            else count = 1;
            max = Math.max(max, count);
        }
        return max;
    }
}