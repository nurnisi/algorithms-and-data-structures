import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        e4_2();
    }

    static void e4_2() {
        String n = sc.nextLine();
        int div = sc.nextInt();

        int[] num = new int[n.length()];
        for (int i = 0; i < n.length(); i++) num[i] = n.charAt(i) - '0';

        if (num[0] == 0) {
            System.out.println(0 + "\n" + 0);
            return;
        }

        int rem = 0;
        for (int i = 0; i < num.length; i++) {
            rem = rem * 10 + num[i];
            num[i] = rem / div;
            rem = rem % div;
        }

        int i = 0;
        while (num[i] == 0) i++;
        while (i < num.length) System.out.print(num[i++]);
        System.out.println("\n" + rem);
    }

    //my attempt: partial solution
    static void e4() {
        String s = sc.nextLine();
        int n = sc.nextInt();
        StringBuilder div = new StringBuilder();
        int cur = s.charAt(0) - '0', i = 1;

        if (s.length() <= 18) System.out.println(Long.valueOf(s) / n + "\n" + Long.valueOf(s) % n);
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