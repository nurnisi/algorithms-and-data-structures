import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.right = new TreeNode(5);
        System.out.println(binaryTreePaths(root));
    }

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public static List<String> binaryTreePaths(TreeNode root) {
        List<String> list = new ArrayList<>();
        if (root != null) helper(root, new ArrayList<>(), list);
        return list;
    }

    public static void helper(TreeNode node, List<Integer> cur, List<String> list) {
        cur.add(node.val);
        if (node.left == null && node.right == null) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < cur.size() - 1; i++) {
                sb.append(cur.get(i));
                sb.append("->");
            }
            sb.append(cur.get(cur.size() - 1));
            list.add(sb.toString());
        } else {
            if (node.left != null) helper(node.left, cur, list);
            if (node.right != null) helper(node.right, cur, list);
        }
        cur.remove(cur.size() - 1);
    }
}