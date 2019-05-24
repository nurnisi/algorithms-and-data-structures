//recursive
public TreeNode invertTree(TreeNode root) {
    if(root != null) {
        TreeNode temp = root.right;
        root.right = invertTree(root.left);
        root.left = invertTree(temp);
    }
    return root;
}

//DFS - depth first search
public TreeNode invertTreeDFS(TreeNode root) {
    if(root == null) return null;

    final Deque<TreeNode> stack = new LinkedList<>();
    stack.push(root);
    while(!stack.isEmpty()) {
        TreeNode node = stack.pop();
        TreeNode temp = node.left;
        node.left = node.right;
        node.right = temp;

        if(node.left != null) stack.push(node.left);
        if(node.right != null) stack.push(node.right);
    }
    return root;
}

//BFS - breadth first search
public TreeNode invertTreeBFS(TreeNode root) {
    if(root == null) return null;

    final Queue<TreeNode> queue = new LinkedList<>();
    queue.offer(root);
    while(!queue.isEmpty()) {
      TreeNode node = queue.poll();
      TreeNode temp = node.left;
      node.left = node.right;
      node.right = temp;

      if(node.left != null) queue.offer(node.left);
      if(node.right != null) queue.offer(node.right)
    }
    return root;
}
