import java.io.*;
import java.util.*;

public class main {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        String str = sc.nextLine();
        String hello = "hello";
        int j = 0;
        for (int i = 0; i < str.length() && j < hello.length(); i++) {
             if (str.charAt(i) == hello.charAt(j)) j++;
        }

        if (j == hello.length()) System.out.println("YES");
        else System.out.println("NO");
    }
}

