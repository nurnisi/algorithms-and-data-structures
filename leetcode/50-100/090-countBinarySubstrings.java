import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(countBinarySubstrings("00110011"));
    }

    //check
    //without auxiliary space
    public static int countBinarySubstrings(String s) {
        int cur = 1, prev = 0, ans = 0;
        for (int i = 0; i < s.length(); i++, cur++)
            if (i + 1 == s.length() || s.charAt(i) != s.charAt(i+1)) {
                ans += Math.min(prev, cur);
                prev = cur;
                cur = 0;
            }
        return ans;
    }

    //with auxiliary space
    public static int countBinarySubstrings2(String s) {
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
