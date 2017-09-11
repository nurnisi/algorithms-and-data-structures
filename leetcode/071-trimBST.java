public TreeNode trimBST(TreeNode root, int L, int R) {
    LinkedList<Integer> list = new LinkedList<>();
    // add elements to list
    trimBST(root, L, R, list);

    // create new tree from list
    TreeNode newRoot = new TreeNode(list.removeFirst());
    for (int value : list)
        insert(newRoot, value);

    return  newRoot;
}

public void trimBST(TreeNode node, int L, int R, LinkedList<Integer> list) {
    if (node == null) return;

    if (node.val >= L && node.val <= R) list.addLast(node.val);

    trimBST(node.left, L, R, list);
    trimBST(node.right, L, R, list);
}

public void insert(TreeNode node, int value) {
    if (value <= node.val) {
        if (node.left == null) node.left = new TreeNode(value);
        else insert(node.left, value);
    } else {
        if (node.right == null) node.right = new TreeNode(value);
        else insert(node.right, value);
    }
}

// leetcode
public TreeNode trimBST(TreeNode root, int L, int R) {
    if (root == null) return null;

    if (root.val > R) return trimBST(root.left, L, R);
    if (root.val < L) return trimBST(root.right, L, R);

    root.left = trimBST(root.left, L, R);
    root.right = trimBST(root.right, L, R);
}