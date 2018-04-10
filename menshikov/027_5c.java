import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        c5_3();
    }

    //with one 2D array
    static void c5_3() {
        int N = sc.nextInt(), K = sc.nextInt();

        int[][] A = new int[N + 2][N + 2];
        for (int i = 1; i < N + 1; i++)
            for (int j = 1; j < N + 1; j++)
                A[i][j] = sc.nextInt();

        long[][] M = new long[N + 2][N + 2];
        M[1][1] = A[1][1];

        for (int k = 1; k < K; k++)
            for (int i = 1; i < N + 1; i++)
                for (int j = 1; j < N + 1; j++)
                    if (k % 2 == (i + j) % 2) {
                        long max = Math.max(Math.max(M[i - 1][j], M[i + 1][j]), Math.max(M[i][j - 1], M[i][j + 1]));
                        M[i][j] = max == 0 ? 0 : (max + A[i][j]);
                    }

        long max = Long.MIN_VALUE;
        for (int i = 1; i < N + 1; i++)
            for (int j = 1; j < N + 1; j++)
                max = Math.max(M[i][j], max);

        System.out.println(max);
    }

    //with 3D array with depth of 2
    static void c5_2() {
        int N = sc.nextInt(), K = sc.nextInt();

        int[][] A = new int[N + 2][N + 2];
        for (int i = 1; i < N + 1; i++)
            for (int j = 1; j < N + 1; j++)
                A[i][j] = sc.nextInt();

        long[][][] M = new long[N + 2][N + 2][2];
        M[1][1][0] = A[1][1];
        for (int k = 1; k < K; k++) {
            for (int i = 1; i < N + 1; i++)
                for (int j = 1; j < N + 1; j++) {
                    long max = Math.max(Math.max(M[i - 1][j][0], M[i + 1][j][0]), Math.max(M[i][j - 1][0], M[i][j + 1][0]));
                    M[i][j][1] = max == 0 ? 0 : (max + A[i][j]);
                }

            for (int i = 1; i < N + 1; i++)
                for (int j = 1; j < N + 1; j++)
                    M[i][j][0] = M[i][j][1];
        }

        long max = Long.MIN_VALUE;
        for (int i = 1; i < N + 1; i++)
            for (int j = 1; j < N + 1; j++)
                max = Math.max(M[i][j][0], max);

        System.out.println(max);
    }

    //with 3D array with depth of K
    static void c5() {
        int N = sc.nextInt(), K = sc.nextInt();

        int[][] A = new int[N + 2][N + 2];
        for (int i = 1; i < N + 1; i++)
            for (int j = 1; j < N + 1; j++)
                A[i][j] = sc.nextInt();

        long[][][] M = new long[N + 2][N + 2][K];
        M[1][1][0] = A[1][1];
        for (int k = 1; k < K; k++)
            for (int i = 1; i < N + 1; i++)
                for (int j = 1; j < N + 1; j++) {
                    long max = Math.max(Math.max(M[i - 1][j][k - 1], M[i + 1][j][k - 1]), Math.max(M[i][j - 1][k - 1], M[i][j + 1][k - 1]));
                    M[i][j][k] = max == 0 ? 0 : (max + A[i][j]);
                }

        long max = Long.MIN_VALUE;
        for (int i = 1; i < N + 1; i++)
            for (int j = 1; j < N + 1; j++)
                max = Math.max(M[i][j][K - 1], max);

        System.out.println(max);
    }
}