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

//CTCI: DFS
List<LinkedList<TreeNode>> listOfDepths(TreeNode root) {
    List<LinkedList<TreeNode>> lists = new ArrayList<>();
    listOfDepths(root, lists, 0);
    return lists;
}

void listOfDepths(TreeNode root, List<LinkedList<TreeNode>> lists, int level) {
    if (root == null) return;

    LinkedList<TreeNode> list = null;
    if (lists.size() == level) {
        list = new LinkedList<>();
        lists.add(list);
    } else {
        list = lists.get(level);
    }

    list.add(root);
    listOfDepths(root.left, lists, level + 1);
    listOfDepths(root.right, lists, level + 1);
}

//CTCI: BFS
List<LinkedList<TreeNode>> listOfDepths(TreeNode root) {
    List<LinkedList<TreeNode>> result = new ArrayList<>();

    LinkedList<TreeNode> current = new LinkedList<>();
    if (root != null) current.add(root);

    while (current.size() > 0) {
        result.add(current);
        LinkedList<TreeNode> parents = current;
        current = new LinkedList<>();

        for (TreeNode parent : parents) {
            if (parent.left != null) current.add(parent.left);
            if (parent.right != null) current.add(parent.right);
        }
    }

    return result;
}