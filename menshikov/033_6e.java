import java.io.*;
import java.util.*;

public class acmp {

    static PrintWriter pw;
    static Scanner sc;

    public static void main(String[] args) throws IOException {
        e6();
    }

    static void e6() throws IOException {
        sc = new Scanner(new File("input.txt"));
        pw = new PrintWriter(new File("output.txt"));

        int N = sc.nextInt();
        int[][] arr = new int[N + 2][N + 2];

        int wall = -1, free = -2, xi = 0, xj = 0;

        for (int i = 0; i < N + 2; i++)
            for (int j = 0; j < N + 2; j++)
                arr[i][j] = wall;

        for (int i = 1; i < N + 1; i++) {
            String cur = sc.next();
            for (int j = 1; j < N + 1; j++) {
                int ch = cur.charAt(j - 1);
                if (ch - '.' == 0) arr[i][j] = free;
                else if (ch - 'O' == 0) arr[i][j] = wall;
                else if (ch - 'X' == 0) {
                    xi = i;
                    xj = j;
                    arr[i][j] = free;
                } else if (ch - '@' == 0) arr[i][j] = 0;
            }
        }

        int k = 0;
        boolean check;

        do {
            check = false;
            for (int i = 1; i < N + 1; i++) {
                for (int j = 1; j < N + 1; j++) {
                    if (arr[i][j] == k) {
                        if (arr[i - 1][j] != wall && arr[i - 1][j] == free) {
                            arr[i - 1][j] = k + 1;
                            check = true;
                        }
                        if (arr[i + 1][j] != wall && arr[i + 1][j] == free) {
                            arr[i + 1][j] = k + 1;
                            check = true;
                        }
                        if (arr[i][j - 1] != wall && arr[i][j - 1] == free) {
                            arr[i][j - 1] = k + 1;
                            check = true;
                        }
                        if (arr[i][j + 1] != wall && arr[i][j + 1] == free) {
                            arr[i][j + 1] = k + 1;
                            check = true;
                        }
                    }
                }
            }
            k++;
        } while (check);

        if (arr[xi][xj] == free) pw.println("N");
        else {
            pw.println("Y");
            int path = -3;
            while (arr[xi][xj] != 0) {
                int xij = arr[xi][xj];
                arr[xi][xj] = path;
                if (arr[xi - 1][xj] == xij - 1) xi--;
                else if (arr[xi + 1][xj] == xij - 1) xi++;
                else if (arr[xi][xj - 1] == xij - 1) xj--;
                else if (arr[xi][xj + 1] == xij - 1) xj++;
            }

            for (int i = 1; i < N + 1; i++) {
                for (int j = 1; j < N + 1; j++) {
                    if (arr[i][j] == wall) pw.print("O");
                    else if (arr[i][j] == path) pw.print("+");
                    else if (arr[i][j] == 0) pw.print("@");
                    else pw.print(".");
                }
                pw.println();
            }
        }

        pw.close();
    }
}