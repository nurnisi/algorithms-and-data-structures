public static List<Double> averageOfLevels(TreeNode root) {
    List<Double> result = new ArrayList<>();
    Queue<TreeNode> queue = new LinkedList<>();

    if (root == null) return result;
    queue.add(root);
    while (!queue.isEmpty()) {
        int n = queue.size();
        double sum = 0;
        for (int i = 0; i < n; i++) {
            TreeNode node = queue.remove();
            sum += node.val;

            if (node.left != null) queue.add(node.left);
            if (node.right != null) queue.add(node.right);
        }
        result.add(sum / n);
    }
    return result;
}
