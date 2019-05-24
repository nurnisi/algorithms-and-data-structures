import java.util.*;

public class leetcode {

    public static void main(String[] args) {

    }

    public int dominantIndex(int[] nums) {
        int index = 0;
        for (int i = 0; i < nums.length; i++)
            if (nums[index] < nums[i])
                index = i;

        for (int i = 0; i < nums.length; i++)
            if (i != index && nums[i] * 2 > nums[index])
                return -1;

        return index;
    }
}