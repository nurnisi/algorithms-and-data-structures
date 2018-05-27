import java.util.*;

public class leetcode {

    public static void main(String[] args) {

    }
    //3
    int min, ans = Integer.MAX_VALUE;
    public int findSecondMinimumValue(TreeNode root) {
        min = root.val;
        dfs(root);
        return ans != Integer.MAX_VALUE ? ans : -1;
    }

    public void dfs(TreeNode node) {
        if (node != null) {
            if (min < node.val && node.val < ans) ans = node.val;
            else if (min == node.val) {
                dfs(node.left);
                dfs(node.right);
            }
        }
    }

    //2
    public int findSecondMinimumValue3(TreeNode root) {
        Set<Integer> set = new TreeSet<>();
        dfs(root, set);

        int min = root.val, ans = Integer.MAX_VALUE;
        for (int i : set)
            if (i > min) {
                ans = i;
                break;
            }
        return ans != Integer.MAX_VALUE ? ans : -1;
    }

    public void dfs(TreeNode node, Set<Integer> set) {
        if (node != null) {
            set.add(node.val);
            dfs(node.left, set);
            dfs(node.right, set);
        }
    }

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    //1
    public int findSecondMinimumValue2(TreeNode root) {
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