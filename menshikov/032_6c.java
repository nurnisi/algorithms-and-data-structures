import java.io.*;
import java.util.*;

public class acmp {

    static PrintWriter pw;
    static Scanner sc;

    public static void main(String[] args) throws IOException {
        c6();
    }

    static int[] daysInMonth = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 30};

    static void c6() throws IOException {
        sc = new Scanner(new File("input.txt"));
        pw = new PrintWriter(new File("output.txt"));

        int day = sc.nextInt(), month = sc.nextInt();

        boolean[][] win = new boolean[13][32];
        win[12][31] = true;

        for (int i = daysInMonth.length - 1; i >= 1; i--) {
            for (int j = daysInMonth[i]; j >= 1; j--) {
                if (isValid(i + 2, j) && !win[i + 2][j]) win[i][j] = true;
                else if (isValid(i + 1, j) && !win[i + 1][j]) win[i][j] = true;
                else if (isValid(i, j + 2) && !win[i][j + 2]) win[i][j] = true;
                else if (isValid(i, j + 1) && !win[i][j + 1]) win[i][j] = true;
            }
        }

        if (win[month][day]) pw.print(1);
        else pw.print(2);

        pw.close();
    }

    static boolean isValid(int month, int day) {
        if (month > 12 || day > daysInMonth[month]) return false;
        return true;
    }
}