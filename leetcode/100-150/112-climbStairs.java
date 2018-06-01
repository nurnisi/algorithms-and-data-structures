import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(climbStairs(45));
    }

    //recursive
    public static int climbStairs(int n) {
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