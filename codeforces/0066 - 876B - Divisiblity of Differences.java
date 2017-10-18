import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        b();
    }

    static void b() {
        int n = sc.nextInt();
        int k = sc.nextInt();
        int m = sc.nextInt();

        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int cur = sc.nextInt();
            List<Integer> list = map.getOrDefault(cur % m, new ArrayList<>());
            list.add(cur);
            map.put(cur % m, list);
            if (list.size() == k) {
                System.out.println("Yes");
                for (int j : list) System.out.print(j + " ");
                return;
            }
        }

        System.out.println("No");
    }
}