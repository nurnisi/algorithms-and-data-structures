import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        gravity();
    }

    static void gravity() {
        int n = sc.nextInt();

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        Arrays.sort(arr);

        for (int i : arr) System.out.print(i + " ");
    }
}