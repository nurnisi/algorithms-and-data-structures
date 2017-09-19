// http://codeforces.com/problemset/problem/467/A

import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        nearlyLuckyNumber();
    }

    static void george() {
        int n = Integer.parseInt(sc.nextLine());

        int count = 0;
        for (int i = 0; i < n; i++) {
            int p = sc.nextInt();
            int q = sc.nextInt();

            if (q - p >= 2) count++;
        }

        System.out.println(count);
    }

}