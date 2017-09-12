import java.io.*;
import java.util.*;

public class main {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        String str1 = sc.nextLine().toLowerCase();
        String str2 = sc.nextLine().toLowerCase();

        if (str1.length() != str2.length()) {
            if (str1.length() < str2.length()) System.out.println(-1);
            else System.out.println(1);
        }

        for (int i = 0; i < str1.length(); i++) {
            if (str1.charAt(i) < str2.charAt(i)) {
                System.out.println(-1);
                return;
            } else if (str2.charAt(i) < str1.charAt(i)) {
                System.out.println(1);
                return;
            }
        }

        System.out.println(0);
    }
}
