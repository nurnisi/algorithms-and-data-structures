import java.io.*;
import java.util.*;

public class acmp {

    static PrintWriter pw;
    static Scanner sc;

    public static void main(String[] args) throws IOException {
        b7();
    }

    static int res = 0;

    static void b7() throws IOException {
        sc = new Scanner(new File("input.txt"));
        pw = new PrintWriter(new File("output.txt"));

        String s = sc.next();

        int[] indexes = new int[s.length()];
        int len = 0;

        for (int i = 0; i < s.length() - 1; i++) {
            int a = s.charAt(i) - '0', b = s.charAt(i + 1) - '0';
            if (a != 0 && a * 10 + b <= 33) indexes[len++] = i;
        }

        for (int i = 0; i < len; i++) {
            rec(i, len, indexes);
            res++;
        }

        pw.println(res++);
        pw.close();
    }

    static void rec(int cur, int len, int[] indexes) {
        if (cur < len) {
            int i = cur;
            while (i < len && indexes[i] - indexes[cur] < 1) i++;
            for (; i < len; i++) {
                rec(i, len, indexes);
                res++;
            }
        }
    }
}