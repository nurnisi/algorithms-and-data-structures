import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(climbStairs(6));
    }

    //Binets Method: uses matrix multiplication to obtain the n^​th Fibonacci Number
    public static int climbStairs(int n) {
        int[][] q = {{1,1},{1,0}};
        int[][] res = pow(q, n);
        return res[0][0];
    }

    public static int[][] pow(int[][] a, int n) {
        int[][] ret = {{1,0},{0,1}};
        while (n > 0) {
            if ((n & 1) == 1) {
                ret = multiply(ret, a);
            }
            n >>= 1;
            a = multiply(a, a);
        }
        return ret;
    }

    public static int[][] multiply(int[][] a, int[][] b) {
        int[][] c = new int[2][2];
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j];
            }
        }
        return c;
    }

    //dp
    public static int climbStairs6(int n) {
        if (n == 1) return 1;
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++) dp[i] = dp[i - 1] + dp[i - 2];
        return dp[n];
    }

    //recursion with memorization
    public static int climbStairs5(int n) {
        return helper(0, n, new int[n]);
    }

    public static int helper(int i, int n, int[] memo) {
        if (i > n) return 0;
        if (i == n) return 1;
        if (memo[i] > 0) return memo[i];
        memo[i] = helper(i + 1, n, memo) + helper(i + 2, n, memo);
        return memo[i];
    }

    //recursive
    public static int climbStairs4(int n) {
        return helper(0, n);
    }

    public static int helper(int i, int n) {
        if (i > n) return 0;
        if (i == n) return 1;
        return helper(i + 1, n) + helper(i + 2, n);
    }

    //recursive
    public static int climbStairs3(int n) {
        if (n <= 1) return 1;
        return climbStairs(n - 1) + climbStairs(n - 2);
    }

    //iterative
    public static int climbStairs2(int n) {
        if (n <= 3) return n;
        int ii = 2, jj = 3, cur = 4;
        while (cur <= n) {
            int temp = jj;
            jj += ii;
            ii = temp;
            cur++;
        }
        return jj;
    }
}