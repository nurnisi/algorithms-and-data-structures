    boolean check = true;
    public boolean isSymmetric(TreeNode root) {
        if (root == null) return true;
        Stack<Integer> stack = new Stack<>();
        helper(root.left, false, stack);
        helper(root.right, true, stack);
        return stack.isEmpty() && check;
    }
    
    public void helper(TreeNode node, boolean flag, Stack<Integer> stack) {
        if (node == null) return;
        if (!flag) {
            helper(node.left, flag, stack);
            stack.push(node.val);
            helper(node.right, flag, stack);
        } else {
            helper(node.left, flag, stack);
            if (stack.isEmpty() || node.val != stack.pop()) {
                check = false;
                return;
            }
            helper(node.right, flag, stack);
        }
    }