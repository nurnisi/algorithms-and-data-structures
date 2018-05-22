import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(readBinaryWatch(1));
        System.out.println(res.size());
    }

    //iterative
    public static List<String> readBinaryWatch(int num) {
        List<String> res = new ArrayList<>();
        for (int h = 0; h < 12; h++)
            for (int m = 0; m < 60; m++)
                if (Integer.bitCount((h << 6) + m) == num)
                    res.add(String.format("%d:%02d", h, m));
        return res;
    }

    //my solution: DFS permutation
    static int num;
    static List<String> res = new ArrayList<>();
    public static List<String> readBinaryWatch2(int num) {
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