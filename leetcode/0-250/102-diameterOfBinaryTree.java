import java.util.*;

public class leetcode {

    public static void main(String[] args) {

    }

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }


    int diam = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        helper(root);
        return diam;
    }

    public int helper(TreeNode node) {
        if (node == null) return 0;
        int left = helper(node.left),
            right = helper(node.right);
        diam = Math.max(diam, left + right);
        return Math.max(left, right) + 1;
    }
}