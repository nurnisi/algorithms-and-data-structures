import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(rotateString("abcde", "cdeba"));
    }

    public static boolean rotateString(String A, String B) {
        return A.length() == B.length() && (A + A).contains(B);
    }

    public static boolean rotateString3(String A, String B) {
        if (A.length() != B.length()) return false;
        if (A.length() == 0) return true;

        search:
        for (int s = 0; s < A.length(); s++) {
            for (int i = 0; i < A.length(); i++) {
                if (A.charAt((s + i) % A.length()) != B.charAt(i))
                    continue search;
            }
            return true;
        }
        return false;
    }

    public static boolean rotateString2(String A, String B) {
        if (A.equals(B)) return true;
        StringBuilder sb = new StringBuilder(A);
        for (int i = 0; i < A.length(); i++) {
            if (sb.toString().equals(B)) return true;
            sb.append(A.charAt(i));
            sb.deleteCharAt(0);
        }
        return false;
    }
}
