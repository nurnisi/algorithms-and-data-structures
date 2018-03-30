import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        f3();
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