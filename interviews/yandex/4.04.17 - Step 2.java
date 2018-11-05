import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        fixSum();
    }

    //4
    static void fixSum() {
        long s = sc.nextInt(),
            l1 = sc.nextInt(),
            r1 = sc.nextInt(),
            l2 = sc.nextInt(),
            r2 = sc.nextInt();

        boolean check = true;
        while (l1 <= r1) {
            long m = s - l1;
            if (l2 <= m && m <= r2) {
                System.out.println(l1 + " " + (m));
                check = false;
                break;
            }
            l1++;
        }

        if (check) System.out.println(-1);
    }

    //3
    static void different() {
        int n = sc.nextInt();
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < n; i++) {
            int next = sc.nextInt();
            if (!set.contains(next)) set.add(next);
        }
        System.out.println(set.size());
    }

    //2
    static void power2() {
        long n = sc.nextInt();
        long m = 1, res = 0;
        while (m <= n) {
            res++;
            m *= 2;
        }
        System.out.println(res);
    }

    //1
    static void top5() {
        BST tree = new BST();
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            tree.insert(sc.nextInt());
            tree.inorder();
            for (int j = i < 4 ? i : 4; j >= 0; j--) {
                System.out.print(tree.arr[j] + " ");
            }
            System.out.println();
        }
    }

    static class BST {
        class Node {
            int key;
            Node left, right;

            public Node(int item) {
                key = item;
                left = right = null;
            }
        }

        Node root;
        int[] arr;
        int cur;

        BST() {
            root = null;
            arr = new int[5];
        }

        void insert(int key) {
            root = insert(root, key);
        }

        Node insert(Node root, int key) {
            if (root == null) {
                root = new Node(key);
                return root;
            }

            if (key < root.key)
                root.left = insert(root.left, key);
            else if (key > root.key)
                root.right = insert(root.right, key);

            return root;
        }

        void inorder() {
            cur = 0;
            inorder(root);
        }

        void inorder(Node root) {
            if (root != null && cur < 5) {
                inorder(root.left);
                arr[cur++] = root.key;
                inorder(root.right);
            }
        }
    }
}