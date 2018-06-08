    public int findLHS(int[] nums) {
        if (nums.length == 0) return 0; 
        Arrays.sort(nums);
        int start = 0, end = 0, prev = 0, prevlen = 0, max = 0;
        while (end <= nums.length) {
            if (end == nums.length || nums[start] != nums[end]) {
                if (nums[start] - 1 == prev)
                    max = Math.max(max, prevlen + end - start);
                prev = nums[start];
                prevlen = end - start;
                if (end == nums.length && start == 0) return 0;
                start = end;
            }
            end++;
        }
        
        return max != 1 ? max : 0;
    }

    //time limit exceeded
    public int findLHS2(int[] nums) {
        int res = 0;
        for (int i = 0; i < (1 << nums.length); i ++) {
            int count = 0, min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
            for (int j = 0; j < nums.length; j++)
                if ((i & (1 << j)) != 0) {
                    min = Math.min(min, nums[j]);
                    max = Math.max(max, nums[j]);
                    count++;
                }
            if (max - min == 1)
                res = Math.max(res, count);
        }
        return res;
    }