import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        e2();
    }

    static void e2() {
        String s1 = sc.next(), s2 = sc.next();

        StringBuilder sb = new StringBuilder();

        int i = s1.length() - 1, j = s2.length() - 1;
        int c = 0;
        while (i >= 0 && j >= 0) {
            int n = (s1.charAt(i--) - '0') + (s2.charAt(j--) - '0') + c;
            sb.append(n % 10);
            c = n / 10;
        }

        while (i >= 0) {
            int n = (s1.charAt(i--) - '0') + c;
            sb.append(n % 10);
            c = n / 10;
        }

        while (j >= 0) {
            int n = (s2.charAt(j--) - '0') + c;
            sb.append(n % 10);
            c = n / 10;
        }

        if (c != 0) sb.append(c);

        System.out.println(sb.reverse().toString());
    }
}