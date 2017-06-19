//mine
public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
    if(t1 == null && t2 == null) return null;
    int t1val = 0, t2val = 0;
    TreeNode node;
    if(t1 == null) {
        node = new TreeNode(t2.val);
        node.left = mergeTrees(null, t2.left);
        node.right = mergeTrees(null, t2.right);
    } else if(t2 == null) {
        node = new TreeNode(t1.val);
        node.left = mergeTrees(t1.left, null);
        node.right = mergeTrees(t1.right, null);
    } else {
        node = new TreeNode(t1.val + t2.val);
        node.left = mergeTrees(t1.left, t2.left);
        node.right = mergeTrees(t1.right, t2.right);
    }
    return node;
}

//refractored
public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
  if(t1 == null && t2 == null) return null;
  int val = (t1 == null ? 0 : t1.val) + (t2 == null ? 0 : t2.val);
  TreeNode node = new TreeNode(val);

  node.left = mergeTrees((t1 == null ? null : t1.left), (t2 == null ? null : t2.left));
  node.right = mergeTrees((t1 == null ? null : t1.right), (t2 == null ? null : t2.right));

  return node;
}
