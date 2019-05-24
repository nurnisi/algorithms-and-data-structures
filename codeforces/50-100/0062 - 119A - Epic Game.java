import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        epicGame();
    }

    static void epicGame() {
        int a = sc.nextInt();
        int b = sc.nextInt();
        int n = sc.nextInt();

        int take = gcd(n, a);
        int counter = 1;
        n -= take;
        while (n >= take) {
            take = (counter % 2 == 1) ? gcd(n, b) : gcd(n, a);
            counter++;
            n-= take;
        }

        System.out.println((counter % 2 == 1) ? 0 : 1);
    }

    static int gcd(int a, int b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }
}