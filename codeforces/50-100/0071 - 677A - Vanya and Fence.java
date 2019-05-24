import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        fence();
    }

    static void fence() {
        int n = sc.nextInt();
        int h = sc.nextInt();

        int res = 0;
        for (int i = 0; i < n; i++) {
            if (sc.nextInt() > h) res += 2;
            else res++;
        }

        System.out.println(res);
    }
}