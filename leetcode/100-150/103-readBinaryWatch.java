import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(readBinaryWatch(0));
        System.out.println(res.size());
    }

    static int num;
    static List<String> res = new ArrayList<>();
    public static List<String> readBinaryWatch(int num) {
        leetcode.num = num;
        helper(0, 0, 0);
        return res;
    }

    public static void helper(int cur, int ones, int time) {
        if (cur == 10) {
            if (ones == num) computeTime(time);
            return;
        }
        helper(cur + 1, ones, time * 2);
        helper(cur + 1, ones + 1, time * 2 + 1);
    }

    public static void computeTime(int time) {
        int minutes = time & 63, hours = time >> 6;
        if (hours < 12 && minutes < 60) {
            StringBuilder sb = new StringBuilder();
            sb.append(hours);
            sb.append(':');
            if (minutes < 10) sb.append(0);
            sb.append(minutes);
            res.add(sb.toString());
        }
    }
}