import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        translation();
    }

    static void translation() {
        String s1 = sc.nextLine();
        String s2 = sc.nextLine();

        int l1 = s1.length(), l2 = s2.length();
        if (l1 != l2) {
            System.out.println("NO");
            return;
        }

        for (int i = 0; i < l1; i++) {
            if (s1.charAt(i) != s2.charAt(l2 - i - 1)) {
                System.out.println("NO");
                return;
            }
        }

        System.out.println("YES");
    }

}