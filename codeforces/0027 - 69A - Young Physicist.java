// http://codeforces.com/problemset/problem/69/A

import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        isIdle();
    }

    static void isIdle() {
        int n = Integer.parseInt(sc.nextLine());

        int x = 0, y = 0, z = 0;
        for (int i = 0; i < n; i++) {
            x += sc.nextInt();
            y += sc.nextInt();
            z += sc.nextInt();
        }

        System.out.println((x == 0 && y ==0 && z == 0) ? "YES" : "NO");
    }
}