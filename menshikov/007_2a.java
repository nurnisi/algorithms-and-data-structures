import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        b2_3();
    }

    static void b2_3() {
        String s = sc.nextLine();
        char[] rez = new char[8];
        boolean[] used = new boolean[8];

        recursion_3(0, s, s.length(), rez, used);
    }

    static void recursion_3(int cur, String s, int len, char[] rez, boolean[] used) {
        if (cur == len) {
            for (int i = 0; i < len; i++) System.out.print(rez[i]);
            System.out.println();
        } else {
            for (int i = 0; i < len; i++) {
                if (!used[i]) {
                    rez[i] = s.charAt(cur);
                    used[i] = !used[i];
                    recursion_3(cur + 1, s, len, rez, used);
                    used[i] = !used[i];
                }
            }
        }
    }

    static void b2_2() {
        String s = sc.nextLine();
        char[] rez = new char[8];
        boolean[] used = new boolean[8];

        recursion_2(0, s, s.length(), rez, used);
    }

    static void recursion_2(int cur, String s, int len, char[] rez, boolean[] used) {
        if (cur == len) {
            for (int i = 0; i < len; i++) System.out.print(rez[i]);
            System.out.println();
        } else {
            for (int i = 0; i < len; i++) {
                if (!used[i]) {
                    rez[cur] = s.charAt(i);
                    used[i] = !used[i];
                    recursion_2(cur + 1, s, len, rez, used);
                    used[i] = !used[i];
                }
            }
        }
    }

    static void b2() {
        String s = sc.nextLine();
        Queue<Character> queue = new LinkedList<>();
        for (char ch : s.toCharArray()) {
            queue.add(ch);
        }
        recursion(queue, new StringBuilder());
    }

    static void recursion(Queue<Character> queue, StringBuilder sb) {
        if (queue.isEmpty()) {
            System.out.println(sb.toString());
            return;
        }
        int size = queue.size();
        for (int i = 0; i < size; i++) {
            char ch = queue.poll();
            sb.append(ch);

            recursion(queue, sb);

            queue.add(ch);
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}