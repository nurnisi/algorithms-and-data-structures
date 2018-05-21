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

    int[] arr;
    public TreeNode sortedArrayToBST(int[] nums) {
        arr = nums;
        return helper(0, arr.length - 1);
    }

    public TreeNode helper(int left, int right) {
        if (left > right) return null;
        int mid = (left + right) / 2;
        TreeNode node = new TreeNode(arr[mid]);
        node.left = helper(left, mid - 1);
        node.right = helper(mid + 1, right);
        return node;
    }
}