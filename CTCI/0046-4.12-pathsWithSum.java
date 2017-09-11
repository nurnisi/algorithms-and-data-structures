int countPathsWithSum(TreeNode root, int targetSum) {
    if (root == null) return 0;
    
    // count paths starting from root
    int pathsFromRoot = countPathsWithSumFromNode(root, targetSum, 0);

    // count paths from left and right
    int pathsFromLeft = countPathsWithSum(root.left, targetSum);
    int pathsFromRight = countPathsWithSum(root.right, targetSum);

    return pathsFromRoot + pathsFromLeft + pathsFromRight;
}

int countPathsWithSumFromNode(TreeNode node, int targetSum, int currentSum) {
    if (node == null) return 0;

    currentSum += node.data;

    int totalPaths = 0;
    if (currentSum == targetSum) totalPaths++;

    totalPaths += countPathsWithSumFromNode(node.left, targetSum, currentSum);
    totalPaths += countPathsWithSumFromNode(node.right, targetSum, currentSum);

    return totalPaths;
}