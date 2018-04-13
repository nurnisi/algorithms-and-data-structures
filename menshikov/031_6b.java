import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        b6();
    }

    //my solution: does not pass time limit
    static int res = 0;
    static int[] arr;
    static boolean[] sums = new boolean[50001];
    static Set<Integer> set = new HashSet<>();

    static void b6() {
        int N = sc.nextInt();
        arr = new int[N];
        for (int i = 0; i < N; i++) arr[i] = sc.nextInt();

        rec(0, N, 0);
        System.out.println(res);
    }

    static void rec(int cur, int N, int curSum) {
        if (cur == N) {
            if (!set.contains(curSum)) {
                res++;
                set.add(curSum);
            }
        } else {
            rec(cur + 1, N, curSum);
            rec(cur + 1, N, curSum + arr[cur]);
        }
    }
}