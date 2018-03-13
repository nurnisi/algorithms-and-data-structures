import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        b3();
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