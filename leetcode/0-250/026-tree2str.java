public String tree2str(TreeNode t) {
    String res = "";
    if(t != null) {
        res += String.valueOf(t.val);
        if(t.left != null) {
            res += "(" + tree2str(t.left) + ")";
        }
        if(t.right != null) {
            if(t.left == null) res += "()";
            res += "(" + tree2str(t.right) + ")";
        }
    }
    return res;
}
