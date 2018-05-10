import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(countBinarySubstrings("10101"));
    }

    public static int countBinarySubstrings(String s) {
        List<Integer> list = new ArrayList<>();
        for (int i = 0, cur = 1; i < s.length(); i++, cur++) {
            if (i + 1 == s.length() || s.charAt(i) != s.charAt(i + 1)) {
                list.add(cur);
                cur = 0;
            }
        }
        int ans = 0;
        for (int i = 0; i < list.size() - 1; i++)
            ans += Math.min(list.get(i), list.get(i + 1));
        return ans;
    }
}
