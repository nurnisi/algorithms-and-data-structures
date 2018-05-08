import java.util.*;

public class leetcode {

    public static void main(String[] args) {

    }

    public List<List<Integer>> largeGroupPositions(String S) {
        List<List<Integer>> res = new ArrayList<>();
        int cur = 0, run = 1;
        for (; run < S.length(); run++) {
            if (S.charAt(cur) != S.charAt(run)) {
                if (run - cur >= 3) res.add(Arrays.asList(cur, run - 1));
                cur = run;
            }
        }
        if (run - cur >= 3) res.add(Arrays.asList(cur, run - 1));
        return res;
    }
}
