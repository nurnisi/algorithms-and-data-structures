public List<Integer> findDisappearedNumbers(int[] nums) {
    Map<Integer, Integer> map = new HashMap<>();
    for(int i : nums) {
        if(map.get(i) == null) map.put(i, 1);
    }

    List<Integer> res = new ArrayList<>();
    for(int j = 1; j <= nums.length; j++) {
        if(map.get(j) == null) res.add(j);
    }
    return res;
}
