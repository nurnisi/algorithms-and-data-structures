import java.io.*;
import java.util.*;

public class acmp {

    static PrintWriter pw;
    static Scanner sc;

    public static void main(String[] args) throws IOException {
        b7_2();
    }

    static void b7_2() throws IOException {
        sc = new Scanner(new File("input.txt"));
        pw = new PrintWriter(new File("output.txt"));

        String s = sc.next();

        String[] res = new String[s.length() + 1];
        res[0] = "1";
        res[1] = "1";

        for (int i = 2; i < res.length; i++) {
            int ii = s.charAt(i - 2) - '0', jj = s.charAt(i - 1) - '0';
            if (10 <= ii * 10 + jj && ii * 10 + jj <= 33) sum(i, res);
            else res[i] = res[i - 1];
        }

        String out = res[res.length - 1];
        for (int i = out.length() - 1; i >= 0; i--) pw.print(out.charAt(i));

        pw.close();
    }

    static void sum(int i, String[] res) {
        String s1 = res[i - 1], s2 = res[i - 2];
        StringBuilder sb = new StringBuilder();
        int c = 0, j = 0;
        for (; j < s2.length(); j++) {
            int s1i = s1.charAt(j) - '0', s2i = s2.charAt(j) - '0';
            c = s1i + s2i + c;
            sb.append(c % 10);
            c /= 10;
        }

        while (j < s1.length()) {
            int s1i = s1.charAt(j++) - '0';
            c = s1i + c;
            sb.append(c % 10);
            c /= 10;
        }

        if (c != 0) sb.append(c);
        res[i] = sb.toString();
    }


    //my solution: exceeds time limit
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

        pw.println(res + 1);
        pw.close();
    }

    static void rec(int cur, int len, int[] indexes) {
        if (cur < len) {
            int i = cur;
            while (i < len && indexes[i] - indexes[cur] < 2) i++;
            for (; i < len; i++) {
                rec(i, len, indexes);
                res++;
            }
        }
    }
}