import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(toGoatLatin("Each word consists of lowercase and uppercase letters only"));
    }

    public static String toGoatLatin(String S) {
        Set<Character> vowels = new HashSet<>();
        for (char ch : new char[]{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'})
            vowels.add(ch);

        StringBuilder ans = new StringBuilder(), as = new StringBuilder();
        for (String word : S.split(" ")) {
            char first = word.charAt(0);
            if (vowels.contains(first))
                ans.append(word);
            else {
                ans.append(word.substring(1));
                ans.append(first);
            }

            as.append('a');
            ans.append("ma");
            ans.append(as.toString());
            ans.append(' ');
        }

        ans.deleteCharAt(ans.length() - 1);
        return ans.toString();
    }

    public static String toGoatLatin2(String S) {
        String[] sp = S.split("\\s+");
        StringBuilder as = new StringBuilder(), res = new StringBuilder(), cur;
        for (int i = 0; i < sp.length; i++) {
            cur = new StringBuilder();
            as.append('a');
            char ch = sp[i].charAt(0);
            if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
                ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
                cur.append(sp[i]);
            } else {
                cur.append(sp[i].substring(1));
                cur.append(ch);
            }

            cur.append("ma");
            cur.append(as.toString());

            res.append(cur.toString());
            res.append(i == sp.length - 1 ? "" : " ");
        }

        return res.toString();
    }
}
