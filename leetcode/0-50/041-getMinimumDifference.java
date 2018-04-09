public int getMinimumDifference(TreeNode root) {
    List<Integer> list = new ArrayList<>();
    Queue<TreeNode> queue = new LinkedList<>();
    queue.add(root);

    while(!queue.isEmpty()) {
        TreeNode node = queue.remove();
        list.add(node.val);

        if(node.left != null) queue.add(node.left);
        if(node.right != null) queue.add(node.right);
    }

    Collections.sort(list);
    int min = Integer.MAX_VALUE;
    for(int i = 1; i < list.size(); i++) {
        min = Math.min(min, (list.get(i) - list.get(i - 1)));
    }

    return min;
}

//BST inorder traversal
int min = Integer.MAX_VALUE;
Integer prev = null;

public int getMinimumDifference(TreeNode root) {
    if(root == null) return min;

    getMinimumDifference(root.left);
    if(root != null) min = Math.min(min, root.val - prev);
    prev = root.val;
    getMinimumDifference(root.right);

    return min;
}

//If not BST - used TreeSet
TreeSet<Integer> set = new TreeSet<>();
int min = Integer.MAX_VALUE;

public int getMinimumDifference(TreeNode root) {
    if(root == null) return min;

    if(!set.isEmpty()) {
        if(set.ceiling(root.val) != null) min = Math.min(min, set.ceiling(root.val) - root.val);
        if(set.floor(root.val) != null) min = Math.min(min, root.val - set.floor(root.val));
    }
    set.add(root.val);

    getMinimumDifference(root.left);
    getMinimumDifference(root.right);

    return min;
}
