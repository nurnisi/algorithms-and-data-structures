import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(rotateString("abcde", "cdeba"));
    }

    public static boolean rotateString(String A, String B) {
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
