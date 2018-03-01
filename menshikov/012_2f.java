import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        f2();
    }

    static void f2() {
        int n = sc.nextInt();
        int[][] arr = new int[n][n];

        for (int i = 0; i < n; i++) arr[0][i] = i + 1;

        int turns = 0, curNum = n - 1, run = 0;
        char[] directions = {'d', 'l', 'u', 'r'};
        int i = 1, j = n - 1, dir = 0;

        for (int k = n + 1; k <= n * n; k++) {
            arr[i][j] = k;
            run++;

            if (curNum == run) {
                turns++;
                if (turns == 2) {
                    curNum--;
                    turns = 0;
                }
                run = 0;
                dir++;
                if (dir == directions.length) dir = 0;
            }

            if (directions[dir] == 'd') i++;
            else if (directions[dir] == 'l') j--;
            else if (directions[dir] == 'u') i--;
            else if (directions[dir] == 'r') j++;
        }

        for (int k = 0; k < n; k++) {
            for (int l = 0; l < n; l++) {
                System.out.print(arr[k][l] + " ");
            }
            System.out.println();
        }
    }
}