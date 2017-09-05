List<LinkedList<TreeNode>> listOfDepths(TreeNode root) {
    List<LinkedList<TreeNode>> list = new ArrayList<>();

    Queue<TreeNode> queue = new LinkedList<>();
    queue.add(root);

    while (!queue.isEmpty()) {
        int size = queue.size();
        LinkedList<TreeNode> linked = new LinkedList<>();

        for (int i = 0; i < size; i++) {
            TreeNode node = queue.remove();
            linked.add(node);
            if (node.left != null) queue.add(node.left);
            if (node.right != null) queue.add(node.right);
        }

        list.add(linked);
    }

    return list;
}