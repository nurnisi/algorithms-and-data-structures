// Solution 1: with links to parents
TreeNode commonAncestor(TreeNode node1, TreeNode node2) {
    int depth1 = depth(node1);
    int depth2 = depth(node2);
    int diff = depth1 - depth2;

    TreeNode longer = diff > 0 ? node1 : node2;
    TreeNode shorter = diff > 0 ? node2 : node1;

    longer = goUpBy(Math.abs(diff), longer);

    while (longer != null && shorter != null && longer != shorter) {
        longer = longer.parent;
        shorter = shorter.parent;
    }

    return longer == null | shorter == null ? null : longer;
}

TreeNode goUpBy(int diff, TreeNode longer) {
    while (longer != null && diff > 0) {
        longer = longer.parent;
        diff--;
    }
    return longer;
}

int depth(TreeNode n) {
    int depth = 0;
    while (n != null) {
        n = n.parent;
        depth++;
    }
    return depth;
}

// Solution 2: with links to parents but with better worst-case runtime
TreeNode commonAncestor(TreeNode root, TreeNode node1, TreeNode node2) {
    if (!covers(root, node1) || !covers(root, node2) return null;
    if (covers(node1, node2)) return node1;
    if (covers(node2, node1)) return node2;

    TreeNode subling = getSubling(node1);
    TreeNode parent = node1.parent;
    while(!covers(subling, node2)) {
        subling = getSubling(parent);
        parent = parent.parent;
    }

    return parent;
}

boolean covers(TreeNode node1, TreeNode node2) {
    if (node1 == null) return false;
    if (node1 == node2) return true;
    return covers(node1.left, node2) || covers(node1.right, node2);
}

TreeNode getSubling(TreeNode node) {
    if (node == null || node.parent == null) return null;
    TreeNode parent = node.parent;
    return parent.left == node ? parent.right : parent.left;
}