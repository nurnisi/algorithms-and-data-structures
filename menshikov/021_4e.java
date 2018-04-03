import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        e4();
    }

    //my attempt: partial solution
    static void e4() {
        String s = sc.nextLine();
        int n = sc.nextInt();
        StringBuilder div = new StringBuilder();
        int cur = s.charAt(0) - '0', i = 1;

        if (s.length() <= 32) System.out.println(Integer.valueOf(s) / n + "\n" + Integer.valueOf(s) % n);
        else {
            while (i < s.length()) {
                if (cur < n) cur = cur * 10 + (s.charAt(i++) - '0');
                if (cur >= n) {
                    div.append(cur / n);
                    cur %= n;
                }
            }
            System.out.println(div.length() == 0 ? 0 : div.toString() + "\n" + cur);
        }
    }
}