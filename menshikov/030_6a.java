import java.lang.reflect.Array;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        a6();
    }

    static void a6() {
        int N = sc.nextInt();
        int[][] arr = new int[N][2];

        for (int i = 0; i < N; i++) {
            arr[i][0] = sc.nextInt();
            arr[i][1] = sc.nextInt();
        }

        Arrays.sort(arr, Comparator.comparingInt(a -> a[0]));
        int res = 0,
            start = arr[0][0], curMax = arr[0][1];

        for (int i = 1; i < N; i++) {
            if (curMax >= arr[i][0]) curMax = Math.max(curMax, arr[i][1]);
            else {
                res += curMax - start;
                start = arr[i][0];
                curMax = arr[i][1];
            }
        }
        res += curMax - start;
        System.out.println(res);
    }
}