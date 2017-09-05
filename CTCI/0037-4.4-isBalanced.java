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