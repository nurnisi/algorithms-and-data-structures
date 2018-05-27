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

    public int findSecondMinimumValue(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        Integer min = root.val, ans = null;
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            if (node.val != min) {
                if (ans == null) ans = node.val;
                else ans = Math.min(node.val, ans);
            }
            if (node.left != null) queue.add(node.left);
            if (node.right != null) queue.add(node.right);
        }
        return ans != null ? ans : -1;
    }
}