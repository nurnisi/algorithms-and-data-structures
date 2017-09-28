import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        arrival();
    }

    static void arrival() {
        int n = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int max = Integer.MIN_VALUE,
                maxIndex = n - 1,
                min = Integer.MAX_VALUE,
                minIndex = 0;

        for (int i = 0, j = n - 1; i < n; i++, j--) {
            if (arr[j] >= max) {
                max = arr[j];
                maxIndex = j;
            }
            if (arr[i] <= min) {
                min = arr[i];
                minIndex = i;
            }
        }

        if (maxIndex > minIndex) System.out.println(maxIndex + n - 1 - minIndex - 1);
        else System.out.println(maxIndex + n - 1 - minIndex);
    }

}