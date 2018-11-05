import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        lanterns();
    }

    static void lanterns() {
        int n = sc.nextInt();
        double l = sc.nextInt();

        double[] arr = new double[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextDouble();
        }

        Arrays.sort(arr);

        double res = arr[0];
        res = Math.max(res, l - arr[n - 1]);

        for (int i = 1; i < n; i++) {
            res = Math.max(res, (arr[i] - arr[i - 1]) / 2);
        }

        System.out.println(res);
    }
}