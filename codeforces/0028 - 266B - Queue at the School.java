// http://codeforces.com/problemset/problem/266/B

import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        queue();
    }

    static void queue() {
        int n = sc.nextInt();
        int t = sc.nextInt();

        String queue = sc.next();
        char[] arr = queue.toCharArray();

        for (int i = 0; i < t; i++) {
            for (int j = 0; j < arr.length - 1; j++) {
                if (arr[j] == 'B' && arr[j + 1] == 'G') {
                    swap(arr, j, j + 1);
                    j++;
                }
            }
        }

        System.out.println(String.valueOf(arr));
    }

    static void swap(char[] arr, int i, int j) {
        char temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}