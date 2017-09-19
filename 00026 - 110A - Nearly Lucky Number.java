// http://codeforces.com/problemset/problem/110/A

import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        nearlyLuckyNumber();
    }

    static void nearlyLuckyNumber() {
        long n = sc.nextLong();

        if (isNearlyLucky(n)) System.out.println("YES");
        else System.out.println("NO");
    }

    static boolean isNearlyLucky(long n) {
        int luckyCount = 0;

        while (n != 0) {
            if (n % 10 == 4 || n % 10 == 7) luckyCount++;
            n /= 10;
        }
        return isLucky(luckyCount);
    }

    static boolean isLucky(long n) {
        if (n == 0) return false;

        while (n != 0) {
            if (n % 10 != 4 && n % 10 != 7) return false;
            n /= 10;
        }

        return true;
    }
}