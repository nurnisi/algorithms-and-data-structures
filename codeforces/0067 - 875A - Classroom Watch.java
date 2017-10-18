import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        c();
    }

    static void c() {
        int n = sc.nextInt();
        
        List<Integer> list = new ArrayList<>();
        for (int i = 100; i >= 1; i--) {
            int k = n - i;
            int sum = 0;
            while (k > 0) {
                sum += k % 10;
                k /= 10;
            }

            if (sum == i) list.add(n - i);
        }

        System.out.println(list.size());
        if (list.size() > 0) {
            for (int i : list) System.out.println(i);
        }
    }
}