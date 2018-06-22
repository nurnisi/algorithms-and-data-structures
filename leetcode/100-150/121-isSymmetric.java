    //my solution: does not work
    boolean check = true;
    public boolean isSymmetric(TreeNode root) {
        if (root == null) return true;
        Stack<Integer> stack = new Stack<>();
        helperFill(root.left, stack);
        helperCheck(root.right, stack);
        return stack.isEmpty() && check;
    }
    
    public void helperFill(TreeNode node, Stack<Integer> stack) {
        if (node == null) stack.push(0);
        else {
            helperFill(node.left, stack);
            stack.push(node.val);
            helperFill(node.right, stack);
        }
    }

    public void helperCheck(TreeNode node, Stack<Integer> stack) {
        if (node == null) {
            if (stack.isEmpty() || stack.pop() != 0) {
                check = false;
                return;
            }
        } else {
            helperCheck(node.left, stack);
            if (stack.isEmpty() || node.val != stack.pop()) {
                check = false;
                return;
            }
            helperCheck(node.right, stack);
        }
    }

    //my solution: acccepted
    public boolean isSymmetric2(TreeNode root) {
        if (root == null) return true;
        Queue<TreeNode> q = new LinkedList<>();
        Queue<Integer> l = new LinkedList<>();
        q.add(root.left);
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = q.remove();
                if (node == null) l.add(0);
                else {
                    l.add(node.val);
                    q.add(node.left);
                    q.add(node.right);
                }
            }
        }

        q.add(root.right);
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = q.remove();
                if (l.isEmpty()) return false;
                else if (node == null) {
                    if (l.remove() != 0) return false;
                }
                else {
                    if (node.val != l.remove()) return false;
                    q.add(node.right);
                    q.add(node.left);
                }
            }
        }
        return true;
    }