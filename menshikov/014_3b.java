import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        b3_2();
    }

    static void b3_2() {
        char[] arr = sc.nextLine().toCharArray();

        recursion(arr, new boolean[arr.length], new char[arr.length], 0, new HashSet<>());
    }

    static void recursion(char[] arr, boolean[] used, char[] res, int n, Set<String> set) {
        if (n == arr.length) {
            String s = String.valueOf(res);
            if (!set.contains(s)) {
                set.add(s);
                System.out.println(s);
            }
        } else {
            for (int i = 0; i < used.length; i++) {
                if (!used[i]) {
                    res[n] = arr[i];
                    used[i] = true;
                    ++n;

                    recursion(arr, used, res, n, set);

                    --n;
                    used[i] = false;
                }
            }
        }
    }

    static void b3() {
        String s = sc.nextLine();

        Queue<Character> queue = new LinkedList<>();
        for (char ch : s.toCharArray()) queue.add(ch);

        recursion(queue, new StringBuilder(), new HashSet<>());
    }

    static void recursion(Queue<Character> queue, StringBuilder sb, Set<String> set) {
        if (queue.isEmpty()) {
            String s1 = sb.toString();
            if (!set.contains(s1)) {
                set.add(s1);
                System.out.println(s1);
            }
        } else {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                char ch = queue.poll();
                sb.append(ch);

                recursion(queue, sb, set);

                queue.add(ch);
                sb.deleteCharAt(sb.length() - 1);
            }
        }
    }

    static void swap(char[] arr, int i, int j) {
        char temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}