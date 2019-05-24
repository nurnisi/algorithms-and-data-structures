
import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        games();
    }

    static void games() {
        int n = sc.nextInt();
        int[] arr = new int[n];
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
            int k = sc.nextInt();
            map.put(k, map.getOrDefault(k, 0) + 1);
        }

        int res = 0;
        for (int i = 0; i < n; i++) {
            res += map.getOrDefault(arr[i], 0);
        }

        System.out.println(res);
    }
}