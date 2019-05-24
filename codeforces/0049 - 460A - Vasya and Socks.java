    static void socks() {
        int n = sc.nextInt();
        int m = sc.nextInt();

        int res = n + Math.floorDiv(n - 1, m - 1);
        System.out.println(res);
    }


import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        socks();
    }

    static void socks() {
        int n = sc.nextInt();
        int m = sc.nextInt();

        int res = n, rem = 0;
        if (n >= m) {
            while (n > rem) {
                rem = n % m;
                n /= m;
                res += n;
                n += rem;
            }
        }

        System.out.println(res);
    }
}