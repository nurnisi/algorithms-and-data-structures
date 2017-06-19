public static int[] intersection(int[] nums1, int[] nums2) {
    Set<Integer> set = new HashSet<>();
    for(int i : nums1)
        if(!set.contains(i))
            set.add(i);

    List<Integer> list = new ArrayList<>();
    for(int j : nums2)
        if(set.contains(j)) {
            list.add(j);
            set.remove(j);
        }

    int[] res = new int[list.size()];
    for (int i = 0; i < list.size(); i++)
        res[i] = list.get(i);

    return res;
}
