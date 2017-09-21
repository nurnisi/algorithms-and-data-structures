import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        insomnia();
    }

    static void insomnia() {
        int k = sc.nextInt(),
            l = sc.nextInt(),
            m = sc.nextInt(),
            n = sc.nextInt(),
            d = sc.nextInt();

        int counter = 0;
        for (int i = 0; i < d; i++) {
            if ((i + 1) % k == 0 || (i + 1) % l == 0
                || (i + 1) % m == 0 || (i + 1) % n == 0) {
                counter++;
            }
        }

        System.out.println(counter);
    }
}

// optimized
import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        insomnia();
    }

    static void insomnia() {
        int k = sc.nextInt(),
            l = sc.nextInt(),
            m = sc.nextInt(),
            n = sc.nextInt(),
            d = sc.nextInt();

        int d1 = d / k + d / l + d / m + d / n;
        int d2 = d / lcm2(k, l) + d / lcm2(k, m) + d / lcm2(k, n) + d / lcm2(l, m) + d / lcm2(l, n) + d / lcm2(m, n);
        int d3 = d / lcm3(k, l, m) + d / lcm3(k, l, n) + d / lcm3(k, m, n) + d / lcm3(l, m, n);
        int d4 = d / lcm4(k, l, m, n);

        System.out.println(d1 - d2 + d3 - d4);
    }

    static int lcm2(int a, int b) {
        return a * b / gcd(a, b);
    }

    static int lcm3(int a, int b, int c) {
        return lcm2(a, lcm2(b, c));
    }

    static int lcm4(int a, int b, int c, int d) {
        return lcm2(lcm2(a, b), lcm2(c, d));
    }

    // non-recursive
    static int gcd(int a, int b) {
        while (b > 0) {
            int temp = a;
            a = b;
            b = temp % b;
        }
        return a;
    }
}