//with array
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

//without array
Integer last_value = null;
boolean isBST(TreeNode node) {
    if (node == null) return true;

    if (!isBST(node.left)) return false;

    if (last_value != null && node.value <= last_value) return false;
    last_value = node.value;

    if (!isBST(node.right)) return false;

    return true;
}

//3
boolean isBST(TreeNode root) {
    return isBST(root, null, null);
}

boolean isBST(TreeNode node, Integer min, Integer max) {
    if (node == null) return true;

    if ((min != null && node.value <= min) || (max != null && node.value > max))
        return false;

    return isBST(node.left, min, node.value) && isBST(node.right, node.value, max);
}