import java.util.*;

public class leetcode {

    public static void main(String[] args) {

    }

    //without helper
    public TreeNode convertBST(TreeNode root) {
        if (root != null) {
            convertBST(root.right);
            sum += root.val;
            root.val = sum;
            convertBST(root.left);
        }
        return root;
    }

    //Definition for a binary tree node.
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public TreeNode convertBST2(TreeNode root) {
        helper(root);
        return root;
    }

    int sum = 0;

    public void helper(TreeNode root) {
        if (root == null) return;
        helper(root.right);
        root.val += sum;
        sum = root.val;
        helper(root.left);
    }
}