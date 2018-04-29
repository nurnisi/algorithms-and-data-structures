import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(countPrimeSetBits2(6, 10));
    }

    public static int countPrimeSetBits2(int L, int R) {
        int ans = 0;
        for (int i = L; i <= R; i++)
            if (isSmallPrime(Integer.bitCount(i)))
                ans++;

        return ans;
    }

    public static boolean isSmallPrime(int n) {
        if (n == 2 || n == 3 || n == 5 || n == 7
            || n == 11 || n == 13 || n == 17 || n == 19) return true;
        return false;
    }

    public static int countPrimeSetBits(int L, int R) {
        int ans = 0;
        while (L <= R) {
            int ones = 0, tempL = L;
            while (tempL > 0) {
                if ((tempL & 1) == 1) ones++;
                tempL >>= 1;
            }
            if (isPrime(ones)) ans++;
            L++;
        }
        return ans;
    }

    public static boolean isPrime(int n) {
        if (n < 2) return false;
        int i = 2;
        while (i * i <= n) {
            if (n % i == 0) return false;
            i++;
        }
        return true;
    }
}
