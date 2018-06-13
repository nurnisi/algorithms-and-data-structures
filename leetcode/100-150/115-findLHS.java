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

    //time limit exceeded
    public int findLHS3(int[] nums) {
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            int count = 0;
            boolean flag = false;
            for (int j = 0; j < nums.length; j++) {
                if (nums[j] == nums[i]) count++;
                else if (nums[j] == nums[i] + 1) {
                    count++;
                    flag = true;
                }
            }
            if (flag) res = Math.max(res, count);
        }
        return res;
    }

    public int findLHS4(int[] nums) {
        Arrays.sort(nums);
        int res = 0, prev_count = 0;
        for (int i = 0; i < nums.length; i++) {
            int count = 1;
            if (i > 0 && nums[i] - nums[i-1] == 1) {
                while (i < nums.length - 1 && nums[i] == nums[i + 1]) {
                    count++;
                    i++;
                }
                res = Math.max(res, count + prev_count);
                prev_count = count;
            } else {
                while (i < nums.length - 1 && nums[i] == nums[i + 1]) {
                    count++;
                    i++;
                }
                prev_count = count;
            }
        }
        return res;
    }

    //using map
    public int findLHS5(int[] nums) {
        Map<Integer,Integer> map = new HashMap<>();
        int res = 0;
        for (int num : nums) map.put(num, map.getOrDefault(num, 0) + 1);
        for (int key : map.keySet())
            if (map.containsKey(key + 1))
                res = Math.max(res, map.get(key) + map.get(key + 1));
        return res;
    }