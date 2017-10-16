import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        transportation();
    }

    static void transportation() {
        int n = sc.nextInt();
        int t = sc.nextInt();

        int[] arr = new int [n - 1];
        for (int i = 0; i < n - 1; i++) {
            arr[i] = sc.nextInt();
        }

        int j = 1;
        while (j < t) {
            j += arr[j - 1];
        }

        if (j == t) System.out.println("YES");
        else System.out.println("NO");
    }
}