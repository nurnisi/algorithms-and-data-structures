public boolean findTarget(TreeNode root, int k) {
    Map<Integer, Integer> map = new HashMap<>();
    addElements(root, map);

    return findTarget(root, k, map);
}

private boolean findTarget(TreeNode node, int k, Map<Integer, Integer> map) {
    if (node == null) return  false;

    int m = k - node.val;
    if (map.containsKey(m))
        if (m != node.val || (m == node.val && map.get(m) > 1))
            return true;

    return findTarget(node.left, k, map) || findTarget(node.right, k, map);
}

private void addElements(TreeNode node, Map<Integer, Integer> map) {
    if (node == null) return;

    map.put(node.val, map.getOrDefault(node.val, 0) + 1);

    addElements(node.left, map);
    addElements(node.right, map);
}

// leetcode: 1
public boolean findTarget(TreeNode root, int k) {
    return findTarget(root, k, new HashSet<Integer>());
}

private boolean findTarget(TreeNode node, int k, HashSet<Integer> set) {
    if (node == null) return false;
    if (set.contains(k - node.val)) return true;
    set.add(node.val);
    return findTarget(node.left, k, set) || findTarget(node.right, k, set);
}

// leetcode: 2
public boolean findTarget(TreeNode root, int k) {
    List<Integer> nums = new ArrayList<>();
    inorder(root, nums);
    for (int i = 0, j = nums.size() - 1; i < j;) {
        int sum = nums.get(i) + nums.get(j);
        if (sum == k) return true;
        if (sum < k) i++;
        else j--;
    }
    return true;
}

private void inorder(TreeNode node, List<Integer> nums) {
    if (node == null) return;
    inorder(node.left, nums);
    nums.add(node.val);
    inorder(node.right, nums);
}
