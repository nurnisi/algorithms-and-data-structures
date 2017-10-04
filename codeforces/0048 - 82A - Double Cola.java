import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        cola();
    }

    static void cola() {
        int n = sc.nextInt();
        int power = 0, sum = 0, next = 0;

        while (n > sum + next) {
            sum += next;
            next = (int) (5 * (Math.pow(2, power++)));
        }

        n -= sum;
        n += next / 5 - 1;
        n /= next / 5;

        if (n == 1) System.out.println("Sheldon");
        if (n == 2) System.out.println("Leonard");
        if (n == 3) System.out.println("Penny");
        if (n == 4) System.out.println("Rajesh");
        if (n == 5) System.out.println("Howard");
    }
}