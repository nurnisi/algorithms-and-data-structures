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

// Alternative approach
boolean containsTree(TreeNode t1, TreeNode t2) {
    if (t2 == null) return true;
    return subTree(t1, t2);
}

boolean subTree(TreeNode t1, TreeNode t2) {
    if (t1 == null) return false;
    else if (t1.data == t2.data && matchTree(t1, t2)) return true;
    return subTree(t1.left, t2) || subTree(t1.right, t2);
}

boolean matchTree(TreeNode t1, TreeNode t2) {
    if (t1 == null && t2 == null) return true;
    else if (t1 == null || t2 == null) return false;
    else if (t1.data != t2.data) return false;
    else return matchTree(t1.left, t2.left) && matchTree(t1.right, t2.right);
}