// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

Task 2
given a tree count
the longest zigzag

class Solution {
    int ans = 0;

    public void solve(Tree T, char prev, int cnt) {
        if (T == null) return;
        ans = Math.max(ans, cnt);
        if (prev == 'L') {
            solve(T.l, 'L', cnt);
            solve(T.r, 'R', cnt + 1);
        } else if (prev == 'R') {
            solve(T.l, 'L', cnt + 1);
            solve(T.r, 'R', cnt);
        }
    }

    public int solution(Tree T) {
        // write your code in Java SE 8
        if(T == null) return 0;

        solve(T.l, 'L', 0);
        solve(T.r, 'R', 0);

        return ans;
    }
}
