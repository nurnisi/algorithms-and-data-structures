import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        word();
    }

    static void word() {
        String s = sc.nextLine();
        int up = 0, low = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) - 'A' <= 25) up++;
            else low++;
        }

        if (up > low) System.out.println(s.toUpperCase());
        else System.out.println(s.toLowerCase());
    }
}