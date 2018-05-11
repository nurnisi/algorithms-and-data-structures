import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(rotatedDigits(857));
    }

    public static int rotatedDigits(int N) {
        int ans = 0;
        for (int i = 1; i <= N; i++) {
            boolean check = false;
            int n = i;
            while (n > 0) {
                int cur = n % 10;
                if (cur == 3 || cur == 4 || cur == 7) {
                    check = false;
                    break;
                }
                if (cur == 2 || cur == 5 || cur == 6 || cur == 9) check = true;
                n /= 10;
            }
            if (check) ans++;
        }
        return ans;
    }
}
