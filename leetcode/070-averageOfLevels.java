//BFS
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

//DFS
static class Node {
    double sum;
    int count;
    public Node(double sum, int count) {
        this.sum = sum;
        this.count = count;
    }
}

public static List<Double> averageOfLevels(TreeNode root) {
    List<Node> temp = new LinkedList<>();
    helper(root, temp, 0);
    List<Double> result = new LinkedList<>();
    for (Node n : temp) {
        result.add(n.sum / n.count);
    }
    return result;
}

private static void helper(TreeNode root, List<Node> temp, int level) {
    if (root == null) return;
    if (level == temp.size()) {
        Node node = new Node((double)root.val, 1);
        temp.add(node);
    } else {
        temp.get(level).sum += root.val;
        temp.get(level).count++;
    }

    helper(root.left, temp, level + 1);
    helper(root.right, temp, level + 1);
}