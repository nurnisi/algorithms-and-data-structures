import java.io.*;
import java.util.*;

public class acmp {

    static PrintWriter pw;
    static Scanner sc;

    public static void main(String[] args) throws IOException {
        f6();
    }

    static void f6() throws IOException {
        sc = new Scanner(new File("input.txt"));
        pw = new PrintWriter(new File("output.txt"));

        int N = sc.nextInt();
        int[][] arr = new int[N + 2][N + 2];

        int wall = -1, free = -2;

        for (int i = 0; i < N + 2; i++)
            for (int j = 0; j < N + 2; j++)
                arr[i][j] = wall;

        for (int i = 1; i < N + 1; i++) {
            String line = sc.next();
            for (int j = 1; j < N + 1; j++)
                if (line.charAt(j - 1) - '.' == 0)
                    arr[i][j] = free;
        }

        int cur = 0;
        boolean check;
        arr[1][1] = 0;
        arr[N][N] = 0;
        do {
            check = false;
            for (int i = 1; i < N + 1; i++) {
                for (int j = 1; j < N + 1; j++) {
                    if (arr[i][j] == cur) {
                        if (arr[i - 1][j] != wall && arr[i - 1][j] == free) {
                            arr[i - 1][j] = cur + 1;
                            check = true;
                        }
                        if (arr[i + 1][j] != wall && arr[i + 1][j] == free) {
                            arr[i + 1][j] = cur + 1;
                            check = true;
                        }
                        if (arr[i][j - 1] != wall && arr[i][j - 1] == free) {
                            arr[i][j - 1] = cur + 1;
                            check = true;
                        }
                        if (arr[i][j + 1] != wall && arr[i][j + 1] == free) {
                            arr[i][j + 1] = cur + 1;
                            check = true;
                        }
                    }
                }
            }
            cur++;
        } while (check);

        int walls = -4;
        for (int i = 1; i < N + 1; i++)
            for (int j = 1; j < N + 1; j++)
                if (arr[i][j] >= 0) {
                    if (arr[i - 1][j] == wall) walls++;
                    if (arr[i + 1][j] == wall) walls++;
                    if (arr[i][j - 1] == wall) walls++;
                    if (arr[i][j + 1] == wall) walls++;
                }

        pw.print(walls * 9);

        pw.close();
    }
}