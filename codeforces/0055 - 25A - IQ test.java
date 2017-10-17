import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        test();
    }

    static void test() {
        int n = sc.nextInt();

        int evens = 0;
        int odds = 0;

        for (int i = 1; i <= n; i++) {
            int cur = sc.nextInt();
            if (cur % 2 == 0) evens++;
            else odds++;

            if (evens == 1 && odds == 1) {
                int run = sc.nextInt();
                if ((cur % 2 == 0 && run % 2 == 0) || (cur % 2 == 1 && run % 2 == 1)) {
                    System.out.println(i - 1);
                } else {
                    System.out.println(i);
                }
                return;
            } else if ((evens >= 2 && odds == 1) || (odds >= 2 && evens == 1)) {
                System.out.println(i);
                return;
            }
        }
    }

    static void test() {
        int n = sc.nextInt();

        int evens = 0, lastEven = 0, lastOdd = 0;

        for (int i = 1; i <= n; i++) {
            int cur = sc.nextInt();
            if (cur % 2 == 0) {
                evens++;
                lastEven = i;
            }
            else lastOdd = i;
        }

        if (evens == 1) System.out.println(lastEven);
        else System.out.println(lastOdd);
    }
}