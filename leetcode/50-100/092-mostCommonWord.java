import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", new String[]{"hit"}));
    }

    public static String mostCommonWord(String paragraph, String[] banned) {
        Set<String> bannedSet = new HashSet<>();
        for (String s : banned) bannedSet.add(s);

        String[] parArray = paragraph.replaceAll("[^a-zA-Z ]", "")
                                    .toLowerCase().split("\\s+");
        Map<String, Integer> map = new HashMap<>();
        for (String s : parArray)
            if (!bannedSet.contains(s))
                map.put(s, map.getOrDefault(s, 0) + 1);

        String ans = parArray[0];
        int max = map.getOrDefault(ans, 0);
        for (String s : map.keySet())
            if (max < map.get(s)) {
                ans = s;
                max = map.get(s);
            }

        return ans;
    }
}
