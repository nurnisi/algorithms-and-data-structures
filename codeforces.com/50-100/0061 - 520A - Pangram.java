import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        pangram();
    }

    static void pangram() {
        int n = Integer.parseInt(sc.nextLine());

        if (n < 26) {
            System.out.println("NO");
            return;
        }

        String s = sc.nextLine().toLowerCase();

        Set<Character> set = new HashSet<>();
        for (int i = 0; i < n; i++) {
            if (!set.contains(s.charAt(i))) set.add(s.charAt(i));
        }

        if (set.size() == 26) System.out.println("YES");
        else System.out.println("NO");
    }
}