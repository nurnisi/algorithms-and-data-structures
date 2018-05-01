import java.util.*;
import java.math.BigInteger;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(rotateString("abcde", "cdeab"));
    }

    public static boolean rotateString(String A, String B) {
        if (A.equals(B)) return true;

        int MOD = 1_000_000_007;
        int P = 113;
        int Pinv = BigInteger.valueOf(P).modInverse(BigInteger.valueOf(MOD)).intValue();

        long hb = 0, power = 1;
        for (char x : B.toCharArray()) {
            hb = (hb + power * x) % MOD;
            power = power * P % MOD;
        }

        long ha = 0; power = 1;
        char[] ca = A.toCharArray();
        for (char x : ca) {
            ha = (ha + power * x) % MOD;
            power = power * P % MOD;
        }

        for (int i = 0; i < ca.length; i++) {
            char x = ca[i];
            ha += power * x - x;
            ha %= MOD;
            ha *= Pinv;
            ha %= MOD;
            if (ha == hb && (A.substring(i + 1) + A.substring(0, i + 1)).equals(B))
                return true;
        }

        return false;
    }

    public static boolean rotateString4(String A, String B) {
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
