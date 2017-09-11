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

// optimized
int countPathsWithSum(TreeNode root, int targetSum) {
    return countPathsWithSum(root, targetSum, 0, new HashMap<Integer, Integer>());
}

int countPathsWithSum(TreeNode node, int targetSum, int runningSum, 
                      HashMap<Integer, Integer> pathCount) {
    if (node == null) return 0;

    // count paths ending at current node
    runningSum += node.data;
    int sum = runningSum - targetSum;
    int totalPaths = pathCount.getOrDefault(sum, 0);

    // if running sum equals target sum, then one additional path starts at root
    if (runningSum == targetSum) totalPaths++;

    incrementHashMap(pathCount, runningSum, 1);
    totalPaths += countPathsWithSum(node.left, targetSum, runningSum, pathCount);
    totalPaths += countPathsWithSum(node.right, targetSum, runningSum, pathCount);
    incrementHashMap(pathCount, runningSum, -1);

    return totalPaths;
}

void incrementHashMap(HashMap<Integer, Integer> map, int key, int delta) {
    int newCount = map.getOrDefault(key, 0) + delta;
    if (newCount == 0) map.remove(key);
    else map.put(key, newCount);
}