import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        beautifulYear();
    }

    static void beautifulYear() {
        int y = sc.nextInt();
        y++;
        while (!isDistinct(y)) y++;

        System.out.println(y);
    }

    static boolean isDistinct(int n) {
        Set<Integer> set = new HashSet<>();
        while (n > 0) {
            if (!set.contains(n % 10)) {
                set.add(n % 10);
                n /= 10;
            } else return false;
        }
        return true;
    }
}