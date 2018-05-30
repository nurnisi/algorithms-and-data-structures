import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(longestWord(new String[]{"w","wo","wor","worl", "world"}));
    }

    public static String longestWord(String[] words) {
        Arrays.sort(words);
        Set<String> set = new HashSet<>();
        set.add("");
        String ans = "";
        for (String w : words) {
            if (set.contains(w.substring(0, w.length() - 1))){
                set.add(w);
                if (w.length() > ans.length()) ans = w;
            }
        }
        return ans;
    }
}