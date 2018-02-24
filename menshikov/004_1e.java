import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        e1();
    }

    static void e1() {
        int a = sc.nextInt(), n = sc.nextInt();
        List<Integer> list = new ArrayList<>();
        list.add(a);

        for (int i = 1; i < n; i++) {
            int k = 0;
            for (int j = 0; j < list.size(); j++) {
                int p = list.get(j) * a + k;
                list.set(j, p % 10);
                k = p / 10;
            }
            if (k != 0) list.add(k);
        }

        for (int i = list.size() - 1; i >= 0; i--) {
            System.out.print(list.get(i));
        }
    }
}