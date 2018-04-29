import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(countPrimeSetBits(10, 15));
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
