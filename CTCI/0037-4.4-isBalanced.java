//not to efficient - O(NlogN)
boolean isBalanced(TreeNode root) {
    if (root == null) return true;

    int heightDiff = getHeight(root.left) - getHeight(root.right);

    if (Math.abs(heightDiff) > 1) return false;
    else return isBalanced(root.left) && isBalanced(root.right);
}

int getHeight(TreeNode node) {
    if (node == null) return -1;
    return Math.max(getHeight(node.left), getHeight(node.right)) + 1;
}

//efficient - O(N)
boolean isBalanced(TreeNode root) {
    return checkHeight(root) != Integer.MIN_VALUE;
}

int checkHeight(TreeNode root) {
    if (root == null) return -1;

    int left_height = checkHeight(root.left);
    if (left_height == Integer.MIN_VALUE) return Integer.MIN_VALUE;

    int right_height = checkHeight(root.right);
    if (right_height == Integer.MIN_VALUE) return Integer.MIN_VALUE;

    int height_diff = Math.abs(left_height - right_height);
    if (height_diff > 1) return Integer.MIN_VALUE;
    else return Math.max(left_height - right_height) + 1;
}