int index = 0;
void isBST(TreeNode node, int[] array) {
    if (node == null) return;
    isBST(node.left);
    array[index++] = node.value;
    isBST(node.right);
}

boolean isBST(TreeNode root) {
    int[] array = new int[root.size];
    isBST(root, array);
    for (int i = 1; i < array.length; i++) {
        if (array[i - 1] > array[i]) return false;
    }
    return true;
}