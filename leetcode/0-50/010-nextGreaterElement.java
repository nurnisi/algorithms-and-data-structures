public int[] nextGreaterElement(int[] findNums, int[] nums) {
    Map<Integer, Integer> map = new HashMap<Integer, Integer>();
    for(int i = 0; i < nums.length; i++) {
        map.put(nums[i], i);
    }

    List<Integer> tempRes = new ArrayList<Integer>();
    for(int j = 0; j < findNums.length; j++) {
        int k = map.get(findNums[j]) + 1;
        int l = -1;
        while(k < nums.length) {
            if(findNums[j] < nums[k]) {
                l = nums[k];
                break;
            }
            k++;
        }
        tempRes.add(l);
    }

    int[] res = new int[tempRes.size()];
    for(int i=0; i < tempRes.size(); i++) {
        res[i] = tempRes.get(i);
    }

    return res;
}

public int[] nextGreaterElementWithStack(int[] findNums, int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        Stack<Integer> stack = new Stack<>();
        for(int i: nums) {
            while(!stack.isEmpty() && stack.peek() < i) {
                map.put(stack.pop(), i);
            }
            stack.push(i);
        }

        for(int j = 0; j < findNums.length; j++)
            findNums[j] = map.getOrDefault(findNums[j], -1);

        return findNums;
    }
