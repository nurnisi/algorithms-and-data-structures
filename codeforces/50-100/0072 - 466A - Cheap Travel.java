import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        rubles();
    }

    static void rubles() {
        int n = sc.nextInt();
        int m = sc.nextInt();
        int a = sc.nextInt();
        int b = sc.nextInt();

        if (b < m * a) {
            int rem = n % m;
            int rubles = n / m * b;
            if (rem * a > b) rubles += b;
            else rubles += a * rem;
            System.out.println(rubles);
        } else {
            System.out.println(a * n);
        }
    }
}