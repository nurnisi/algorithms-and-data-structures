import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        c();
    }

    static void c() {
        int n = sc.nextInt();

        int[] arr = new int[n];

        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        for (int i = 0; i < n; i++) {
            int m = arr[i];
            if (m < 4 || m == 5 || m == 7 || m == 11) System.out.println(-1);
            else {
                if (m % 4 == 0) System.out.println(m / 4);
                else if (m % 4 == 1) System.out.println(1 + (m - 9) / 4);
                else if (m % 4 == 2) System.out.println(1 + (m - 6) / 4);
                else if (m % 4 == 3) System.out.println(2 + (m - 15) / 4);
            }
        }
    }
}