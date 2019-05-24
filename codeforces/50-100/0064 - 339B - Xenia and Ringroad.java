import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        ringroad();
    }

    static void ringroad() {
        int n = sc.nextInt();
        int m = sc.nextInt();

        long res = 0;
        int prev = 1;
        for (int i = 0; i < m; i++) {
            int cur = sc.nextInt();

            if (prev <= cur) res += (cur - prev);
            else res += (n - prev + cur);
            prev = cur;
        }

        System.out.println(res);
    }
}