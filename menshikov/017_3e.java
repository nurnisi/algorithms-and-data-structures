import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        e3();
    }

    static void e3() {
        String s1 = sc.nextLine();
        String s2 = sc.nextLine();

        List<Integer> result = multiply(s1, s2.charAt(s2.length() - 1) - '0', 0);

        int len = s2.length();
        for (int i = len - 2; i >= 0; i--) {
            List<Integer> list = multiply(s1, s2.charAt(i) - '0', len - 1 - i);
            sum(result, list);
        }

        for (int i = result.size() - 1; i >= 0; i--) {
            System.out.print(result.get(i));
        }
    }

    static void sum(List<Integer> result, List<Integer> list) {
        int i = 0, c = 0;
        for (; i < result.size() && i < list.size(); i++) {
            int m = result.get(i) + list.get(i) + c;
            c = m / 10;
            result.set(i, m % 10);
        }

        while (i < list.size()) {
            int m = list.get(i) + c;
            c = m / 10;
            result.add(m % 10);
            i++;
        }

        if (c != 0) result.add(c);
    }

    static List<Integer> multiply(String s, int n, int zeros) {
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < zeros; i++) list.add(0);

        int c = 0, len = s.length();
        for (int i = len - 1; i >= 0; i--) {
            int m = (s.charAt(i) - '0') * n + c;
            c = m / 10;
            list.add(m % 10);
        }
        if (c > 0) list.add(c);

        return list;
    }
}