public static int majorityElement(int[] nums) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i : nums) {
        if (map.containsKey(i)) map.put(i, map.get(i) + 1);
        else map.put(i, 1);
        if (map.get(i) > nums.length/2) return i;
    }
    return 0;
}

//O(1) space and O(n) time solution from leetcode
public static int majorityElement(int[] nums) {
    int major = nums[0], count = 1;
    for (int i = 1; i < nums.length; i++) {
        if (count == 0) {
            count++;
            major = nums[i];
        } else if (major == nums[i]) count++;
        else count--;
    }
    return major;
}
