import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        b4();
    }

    static void b4() {
        int n = sc.nextInt();
        rec(n, 0, 0, new int[n]);
    }

    static void rec(int n, int m, int next, int[] arr) {
        if (n == m) {
            for (int i = 0; i < arr.length; i++) {
                m -= arr[i];
                if (m > 0) System.out.print(arr[i] + "+");
                else {
                    System.out.print(arr[i]);
                    break;
                }
            }
            System.out.println();
        } else {
            for (int i = next == 0 ? 1 : arr[next - 1]; i < n && next < arr.length && m + i <= n; i++) {
                arr[next] = i;
                rec(n, m + i, next + 1, arr);
            }
        }
    }
}