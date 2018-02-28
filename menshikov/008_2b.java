import java.lang.reflect.Array;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        b2();
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