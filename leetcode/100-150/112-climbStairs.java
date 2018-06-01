import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(climbStairs(6));
    }

    public static int climbStairs(int n) {
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