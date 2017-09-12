import java.io.*;
import java.util.*;

public class main {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int i = Integer.parseInt(sc.nextLine());
        int[] arr = new int[5];
        double sum = 0;

        for (int j = 0; j < i; j++) {
            int k = sc.nextInt();
            sum += k;
            arr[k]++;
        }

        sum /= 4;
        sum = Math.ceil(sum);
        if (arr[2] + arr[3] > sum) System.out.println(arr[2] + arr[3]);
        else System.out.println((int) sum);
    }
}

