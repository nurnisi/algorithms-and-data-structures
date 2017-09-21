// http://codeforces.com/problemset/problem/337/A

import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        puzzles();
    }

    static void puzzles() {
        int m = sc.nextInt();
        int n = sc.nextInt();

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        Arrays.sort(arr);
        int res = Integer.MAX_VALUE;
        for (int i = 0; i + m - 1 < n; i++) {
            res = Math.min(res, arr[i + m - 1] - arr[i]);
        }

        System.out.println(res);
    }
}