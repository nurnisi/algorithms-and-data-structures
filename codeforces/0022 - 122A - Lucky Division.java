import java.io.*;
import java.util.*;

public class main {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int num  = sc.nextInt();

        if (isAlmostLucky(num)) System.out.println("YES");
        else System.out.println("NO");
    }

    public static boolean isAlmostLucky(int num) {
        if (isLucky(num)) return true;

        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0 && (isLucky(i) || isLucky(num / i))) {
                return true;
            }
        }

        return false;
    }

    public static boolean isLucky(int num) {
        while (num != 0) {
            if (num % 10 != 4 && num % 10 != 7) {
                return false;
            }
            num /= 10;
        }
        return true;
    }
}