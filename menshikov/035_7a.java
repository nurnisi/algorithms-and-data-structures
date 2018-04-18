import java.io.*;
import java.util.*;

public class acmp {

    static PrintWriter pw;
    static Scanner sc;

    public static void main(String[] args) throws IOException {
        a7_2_farey();
    }

    static void a7_2_farey() throws IOException {
        sc = new Scanner(new File("input.txt"));
        pw = new PrintWriter(new File("output.txt"));

        int N = sc.nextInt();
        int a = 0, b = 1, c = 1, d = N;
        while (c != 1 || d != 1) {
            int k = (N + b) / d, tempC = c, tempD = d;
            c = k * c - a;
            d = k * d - b;
            a = tempC;
            b = tempD;
            pw.println(a + "/" + b);
        }

        pw.close();
    }

    static void a7() throws IOException {
        sc = new Scanner(new File("input.txt"));
        pw = new PrintWriter(new File("output.txt"));

        int N = sc.nextInt();
        Map<Double, String> map = new TreeMap<>();

        for (int i = N; i >= 0; i--) {
            for (int j = 1; j < i; j++) {
                if (gcd(j, i) == 1) {
                    map.put(((double) j) / i, j + "/" + i);
                }
            }
        }

        for (String value : map.values()) pw.println(value);

        pw.close();
    }

    static int gcd(int x, int y) {
        if (y == 0) return x;
        return gcd(y, x % y);
    }
}