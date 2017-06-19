public int singleNumber(int[] nums) {
    Map<Integer, Integer> map = new HashMap<>();
    for(int i : nums) {
        if(map.get(i) == null) map.put(i, 1);
        else if(map.get(i) == 1) map.put(i, 2);
        else if(map.get(i) == 2) map.remove(i);
    }

    int res = 0;
    for(int j : map.keySet()) res = j;
    return res;
}
