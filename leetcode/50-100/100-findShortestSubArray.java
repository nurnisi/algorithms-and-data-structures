import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(findShortestSubArray(new int[]{1,2,2,3,1}));
    }

    public static int findShortestSubArray(int[] nums) {
        Map<Integer, int[]> map = new HashMap<>();
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < nums.length; i++) {
            int[] cur = map.getOrDefault(nums[i], new int[3]);
            if (cur[0] == 0) cur[1] = i;
            cur[0]++;
            cur[2] = i;
            max = Math.max(max, cur[0]);
            map.put(nums[i], cur);
        }

        int ans = Integer.MAX_VALUE;
        for (int i : map.keySet()) {
            int[] cur = map.get(i);
            if (cur[0] == max)
                ans = Math.min(ans, cur[2] - cur[1] + 1);
        }

        return ans;
    }
}