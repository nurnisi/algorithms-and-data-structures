boolean containsTree(TreeNode t1, TreeNode t2) {
    StringBuilder sb1 = new StringBuilder();
    StringBuilder sb2 = new StringBuilder();

    getOrderString(t1, sb1);
    getOrderString(t2, sb2);

    return sb1.indexOf(sb2.toString()) != -1;
}

void getOrderString(TreeNode node, StringBuilder sb) {
    if (node == null) {
        sb.append("X");
        return;
    }

    sb.append(node.data);
    getOrderString(node.left, sb);
    getOrderString(node.right, sb);
}