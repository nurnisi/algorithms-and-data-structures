import java.lang.reflect.Array;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        b6_5();
    }

    //same as b6_4, but counts the result while reading inputs
    static void b6_5() {
        int N = sc.nextInt();

        boolean[] B = new boolean[N * 100 + 1];
        B[0] = true;
        for (int L = 0; L < N; L++) {
            int a = sc.nextInt();
            for (int S = B.length - 1; S >= a; S--) {
                if (B[S - a]) B[S] = true;
            }
        }

        int res = 0;
        for (int i = 0; i < B.length; i++)
            if (B[i])
                res++;

        System.out.println(res);
    }

    //solution with 1 array, also with some minor optimizations
    static void b6_4() {
        int N = sc.nextInt(), max = 0;
        int[] inputs = new int[N];
        for (int i = 0; i < N; i++) {
            inputs[i] = sc.nextInt();
            max += inputs[i];
        }

        boolean[] B = new boolean[max + 1];
        B[0] = true;
        for (int L = 0; L < inputs.length; L++) {
            for (int S = max; S >= inputs[L]; S--) {
                if (B[S - inputs[L]]) B[S] = true;
            }
        }

        int res = 0;
        for (int i = 0; i < B.length; i++)
            if (B[i])
                res++;

        System.out.println(res);
    }

    //solution with 2 arrays
    static void b6_3() {
        int N = sc.nextInt(), max = 0;
        int[] inputs = new int[N];
        for (int i = 0; i < N; i++) {
            inputs[i] = sc.nextInt();
            max += inputs[i];
        }
        boolean[] B1 = new boolean[max + 1],
                  B2 = new boolean[max + 1];
        B1[0] = true;
        for (int L = 1; L <= inputs.length; L++) {
            for (int S = 0; S < B1.length; S++) {
                B2[S] = B1[S];
                if (S - inputs[L - 1] >= 0) B2[S] = B1[S] || B1[S - inputs[L - 1]];
            }
            boolean[] temp = B1;
            B1 = B2;
            B2 = temp;
        }

        int res = 0;
        for (int i = 0; i < B1.length; i++)
            if (B1[i])
                res++;

        System.out.println(res);
    }

    //solution with 2D array
    static void b6_2() {
        int N = sc.nextInt(), max = 0;
        int[] inputs = new int[N];
        for (int i = 0; i < N; i++) {
            inputs[i] = sc.nextInt();
            max += inputs[i];
        }

        boolean[][] B = new boolean[N + 1][max + 1];
        B[0][0] = true;
        for (int L = 1; L < B.length; L++) {
            for (int S = 0; S < B[0].length; S++) {
                B[L][S] = B[L - 1][S];
                if (S - inputs[L - 1] >= 0) B[L][S] = B[L][S] || B[L - 1][S - inputs[L - 1]];
            }
        }

        int res = 0;
        for (int i = 0; i < B[0].length; i++)
            if (B[N][i])
                res++;

        System.out.println(res);
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