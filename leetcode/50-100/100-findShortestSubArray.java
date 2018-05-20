import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(findShortestSubArray(new int[]{1,2,2,3,1}));
    }

    public static int findShortestSubArray(int[] nums) {
        Map<Integer, Integer> left = new HashMap<>(),
                right = new HashMap<>(),
                count = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int x = nums[i];
            if (left.get(x) == null) left.put(x, i);
            right.put(x, i);
            count.put(x, count.getOrDefault(x, 0) + 1);
        }

        int ans = nums.length,
                degree = Collections.max(count.values());
        for (int x : count.keySet()) {
            if (count.get(x) == degree) {
                ans = Math.min(ans, right.get(x) - left.get(x) + 1);
            }
        }
        return ans;
    }

    public static int findShortestSubArray2(int[] nums) {
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