import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(backspaceCompare("a#c", "b"));
    }

    public static boolean backspaceCompare(String S, String T) {
        char[] s = S.toCharArray(), t = T.toCharArray();
        int slen = 0, tlen = 0;
        for (int i = 0; i < s.length; i++) {
            if (s[i] != '#') s[slen++] = s[i];
            else if (slen != 0) slen--;
        }
        for (int i = 0; i < t.length; i++) {
            if (t[i] != '#') t[tlen++] = t[i];
            else if (tlen != 0) tlen--;
        }
        if (slen != tlen) return false;
        for (int i = 0; i < slen; i++)
            if (s[i] != t[i]) return false;
        return true;
    }
}