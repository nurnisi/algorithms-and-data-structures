public static int sumOfLeftLeaves(TreeNode root) {
    if(root == null) return 0;
    return helper(root.left, 'L') + helper(root.right, 'R');
}

public static int helper(TreeNode root, char side) {
    if(root == null) return 0;
    if(root.left == null && root.right == null && side == 'L') return root.val;
    return helper(root.left, 'L') + helper(root.right, 'R');
}
