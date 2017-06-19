public int[] singleNumber(int[] nums) {
    Map<Integer, Integer> map = new HashMap<>();
    for(int i : nums) {
        if(map.get(i) == null) map.put(i, 1);
        else map.remove(i);
    }

    int[] res = new int[2];
    int j = 0;
    for(Integer key: map.keySet()) {
        res[j++] = key;
    }
    return res;
}
