import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        c4_2();
    }

    static void c4_2() {
        int n = sc.nextInt(),
            k = sc.nextInt(),
            t = sc.nextInt();

        int[][] arr = new int[n][3];
        for (int i = 0; i < n; i++) arr[i][0] = sc.nextInt();
        for (int i = 0; i < n; i++) arr[i][1] = sc.nextInt();
        for (int i = 0; i < n; i++) {
            arr[i][2] = sc.nextInt();
            if (arr[i][0] < arr[i][2]) arr[i][1] = 0;
        }

        int[][] M = new int[2][k + 2];
        for (int i = 1; i <= t; i++) {
            int[] A = new int[k + 1];
            for (int j = 0; j < n; j++)
                if (arr[j][0] == i)
                    A[arr[j][2]] += arr[j][1];

            for (int j = 1; j < k + 1; j++)
                M[1][j] = Math.max(M[0][j - 1], Math.max(M[0][j], M[0][j + 1])) + A[j];

            for (int j = 0; j < M[0].length; j++)
                M[0][j] = M[1][j];
        }

        int max = 0;
        for (int i = 0; i < M[0].length; i++) max = Math.max(M[0][i], max);
        System.out.println(max);
    }

    static void c4() {
        int n = sc.nextInt(),
            k = sc.nextInt(),
            t = sc.nextInt();

        int[][] arr = new int[n][3];
        for (int i = 0; i < n; i++) arr[i][0] = sc.nextInt();
        for (int i = 0; i < n; i++) arr[i][1] = sc.nextInt();
        for (int i = 0; i < n; i++) {
            arr[i][2] = sc.nextInt();
            if (arr[i][0] < arr[i][2]) arr[i][1] = 0;
        }

        Arrays.sort(arr, Comparator.comparingInt(a -> a[0]));

        for (int i = 0; i < n; i++) {
            int max = arr[i][1];
            for (int j = 0; j < i; j++) {
                if (Math.abs(arr[i][2] - arr[j][2]) <= arr[i][0] - arr[j][0])
                    max = Math.max(max, arr[i][1] + arr[j][1]);
            }
            arr[i][1] = max;
        }

        int max = arr[0][1];
        for (int i = 1; i < n; i++)
            max = Math.max(max, arr[i][1]);

        System.out.println(max);
    }
}