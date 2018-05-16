import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(romanToInt("MCMXCIV"));
    }

    public static int romanToInt(String s) {
        Map<String, Integer> map = new HashMap<>();
        map.put("I", 1);
        map.put("V", 5);
        map.put("X", 10);
        map.put("L", 50);
        map.put("C", 100);
        map.put("D", 500);
        map.put("M", 1000);
        map.put("IV", 4);
        map.put("IX", 9);
        map.put("XL", 40);
        map.put("XC", 90);
        map.put("CD", 400);
        map.put("CM", 900);

        int ans = 0;
        for (int i = 0; i < s.length(); i++) {
            if (i < s.length() - 1) {
                String temp = s.substring(i, i + 2);
                if (map.containsKey(temp)) {
                    ans += map.get(temp);
                    i++;
                    continue;
                }
            }
            ans += map.get(String.valueOf(s.charAt(i)));
        }
        return ans;
    }
}