import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        f3_2();
    }

    static void f3_2() {
        int n = sc.nextInt();

        int[][] res = new int[n][n];
        int cur = 1;
        for (int c = 0; c < n * 2 - 1; c++) {
            if (c % 2 == 0) {
                for (int i = n - 1; i >= 0; i--) {
                    int j = c - i;
                    if (j >= 0 && j < n) res[i][j] = cur++;
                }
            } else {
                for (int i = 0; i < n; i++) {
                    int j = c - i;
                    if (j >= 0 && j < n) res[i][j] = cur++;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(res[i][j] + " ");
            }
            System.out.println();
        }
    }

    static void f3() {
        int n = sc.nextInt();

        int[][] res = new int[n][n];
        int i = 0, j = 0, dir = 1; // direction: 1 = up, 2 = down
        for (int k = 1; k <= n * n; k++) {
            res[i][j] = k;

            if (dir == 1) {
                if (j == n - 1) {
                    dir = 2;
                    i++;
                } else if (i == 0) {
                    dir = 2;
                    j++;
                } else {
                    i--;
                    j++;
                }
            } else {
                if (i == n - 1) {
                    dir = 1;
                    j++;
                } else if (j == 0) {
                    dir = 1;
                    i++;
                } else {
                    j--;
                    i++;
                }
            }
        }

        for (int k = 0; k < n; k++) {
            for (int l = 0; l < n; l++) {
                System.out.print(res[k][l] + " ");
            }
            System.out.println();
        }
    }
}