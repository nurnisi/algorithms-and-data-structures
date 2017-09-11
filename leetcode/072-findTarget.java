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
