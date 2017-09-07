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