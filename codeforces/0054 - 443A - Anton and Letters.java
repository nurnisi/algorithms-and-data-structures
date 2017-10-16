import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        letters();
    }

    static void letters() {
        String s = sc.nextLine();
        int res = 0;
        boolean[] arr = new boolean[26];
        for (int i = 0; i < s.length(); i++) {
            int j = s.charAt(i) - 'a';
            if (j >= 0 && j <= 25 && !arr[j]) {
                arr[j] = true;
                res++;
            }
        }
        System.out.println(res);
    }
}