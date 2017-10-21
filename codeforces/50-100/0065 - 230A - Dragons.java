import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        dragons();
    }

    static void dragons() {
        int s = sc.nextInt();
        int n = sc.nextInt();

        int[][] arr = new int[n][2];

        for (int i = 0; i < n; i++) {
            arr[i][0] = sc.nextInt();
            arr[i][1] = sc.nextInt();
        }

        Arrays.sort(arr, (o1, o2) -> {
            final Integer int1 = o1[0];
            final Integer int2 = o2[0];
            return int1.compareTo(int2);
        });

        for (int i = 0; i < n; i++) {
            if (s > arr[i][0]) s += arr[i][1];
            else {
                System.out.println("NO");
                return;
            }
        }

        System.out.println("YES");
    }
}