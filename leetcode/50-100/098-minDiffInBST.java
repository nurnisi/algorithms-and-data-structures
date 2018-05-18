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

    //inorder traversal
    Integer min = Integer.MAX_VALUE, pre = null;
    public int minDiffInBST(TreeNode root) {
        if (root.left != null) minDiffInBST(root.left);
        if (pre != null) min = Math.min(min, root.val - pre);
        pre = root.val;
        if (root.right != null) minDiffInBST(root.right);
        return min;
    }

    //my false solution
    static int mini;

    public static int minDiffInBST2(TreeNode root) {
        mini = Integer.MAX_VALUE;
        helper2(root);
        return mini;
    }

    public static int helper2(TreeNode node) {
        if (node == null) return Integer.MAX_VALUE;
        mini = Math.min(Math.abs(helper2(node.left) - node.val), mini);
        mini = Math.min(Math.abs(helper2(node.right) - node.val), mini);
        return node.val;
    }
}