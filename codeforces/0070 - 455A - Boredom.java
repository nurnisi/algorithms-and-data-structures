import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        boredom();
    }

    static void boredom() {
        int n = sc.nextInt();
        long[] arr = new long[100001];

        for (int i = 0; i < n; i++) {
            arr[sc.nextInt()]++;
        }

        long[] ans = new long[100001];
        ans[0] = 0;
        ans[1] = arr[1];

        for (int i = 2; i < ans.length; i++) {
            ans[i] = Math.max(ans[i - 1], ans[i - 2] + arr[i] * i);
        }

        System.out.println(ans[ans.length - 1]);
    }
}