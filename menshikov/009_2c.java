import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        c2();
    }

    static void c2(){
        int n = sc.nextInt();
        int[][] arr = new int[n][n];
        for (int i = 0; i < n; i++) {
            String s = sc.next();
            for (int j = 0; j < n; j++) {
                arr[i][j] = s.charAt(j) - '0';
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) continue;
                else if (i != 0 && j != 0) arr[i][j] += Math.min(arr[i - 1][j], arr[i][j - 1]);
                else if (i == 0) arr[i][j] += arr[i][j - 1];
                else if (j == 0) arr[i][j] += arr[i - 1][j];
            }
        }

        int i = n - 1, j = n - 1;
        while (i != 0 || j != 0) {
            if (i == 0) arr[i][j--] = -1;
            else if (j == 0) arr[i--][j] = -1;
            else if (arr[i - 1][j] > arr[i][j - 1]) arr[i][j--] = -1;
            else arr[i--][j] = -1;
        }

        arr[0][0] = -1;

        for (int k = 0; k < n; k++) {
            for (int l = 0; l < n; l++) {
                System.out.print(arr[k][l] == -1 ? "#" : "-");
            }
            System.out.println();
        }
    }
}